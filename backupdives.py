###
# Deepblu Backup Tool
# by Sander Van de Moortel
# 
# https://github.com/bluppfisk/deepblu-tools
# 
# Connects to Deepblu and backs up dives in UDDF format
# See http://uddf.org for more information on the format
# 
# Requirements: Python <= 3.3, requests, json and jinja2 packages
# Usage: - fill in your login details in the separate login file
#        - then run this script: python3 backupdives.py
#        - find the 
#        

import requests, json, time, jinja2
from datetime import datetime

CHUNKSIZE = 20

DEEPBLU_API = "https://prodcdn.tritondive.co/apis/"
DEEPBLU_LOGIN_API = DEEPBLU_API + "user/v0/login"
DEEPBLU_DIVES_API = DEEPBLU_API + "discover/v0/post/search?postType=divelog&userId="

class DeepbluUser(object):
	def login(self, email, password):
		headers = {
		    "content-type": "application/json; charset=utf-8",
		    "accept-language": "en"
		}
		data = {
		    "email": email,
		    "password": password
		}
		print("Connecting to Deepblu...")
		res = requests.post(DEEPBLU_LOGIN_API, data=json.dumps(data), headers=headers)
		response = json.loads(res.text)

		if response['statusCode'] == 200:
			self.userId = response['result']['userInfo']['ownerId']
			self.authCode = response['result']['accessToken']
			print("Logged in as " + email + '!')
		else:
			print("Could not log in " + email + ", error code: " + str(response['statusCode']))
			self.authCode = None

		return self

class Deepblu(object):
	def loadDivesFromAPI(self, deepbluUser):
		headers = {
			"content-type": "application/json; charset=utf-8",
			"authorization": deepbluUser.authCode,
			"accept-language": "en"
		}

		skip = 0
		posts = []

		print("Loading first " + str(CHUNKSIZE) + " logs from Deepblu API...")
		while skip >= 0:
			res = requests.get(DEEPBLU_DIVES_API + deepbluUser.userId + "&limit=" + str(CHUNKSIZE) + "&skip=" + str(skip), headers=headers)
			response = json.loads(res.text)
			if response['statusCode'] == 200:
				if len(response['result']['posts']) > 0:
					if skip > 0:
						print("Loading next " + str(CHUNKSIZE) + " logs...")

					posts += response['result']['posts']
					skip += CHUNKSIZE
				else:
					print("Found all the logs!")
					skip = -1
			else:
				print("Error obtaining dive logs, error code: " + str(response['statusCode']))
				return False
			
		return DeepbluLogBook(posts)

class DeepbluLogBook(object):
	def __init__(self, logs):
		print ("Parsing...")
		self.logs = []
		for log in logs:
			self.logs.append(DeepbluLog(log['diveLog']))

		self.getUniqueDiveSpots()

	def getUniqueDiveSpots(self):
		self.diveSpots = []
		for log in self.logs:
			if not self.findDiveSpotById(log.diveSpot.id):
				self.diveSpots.append(log.diveSpot)

	def findDiveSpotById(self, diveSpotId):
		for diveSpot in self.diveSpots:
			if diveSpotId == diveSpot.id:
				return diveSpot

		return False


class DeepbluLog(object):
	def __init__(self, jsonLog):
		self.id = 'deepblu_dl_' + jsonLog['divelogId']
		if 'diveDT' in jsonLog: self.diveDate = jsonLog['diveDT']
		if 'airPressure' in jsonLog: self.airPressure = jsonLog['airPressure']
		if 'waterType' in jsonLog: self.waterType = jsonLog['waterType']
		if 'notes' in jsonLog: self.notes = jsonLog['notes']
		if 'diveDuration' in jsonLog: self.diveDuration = jsonLog['diveDuration']
		if 'diveMinTemperature' in jsonLog: self.minTemp = DeepbluTools().convertTemp(jsonLog['diveMinTemperature'])
		if 'diveMaxDepth' in jsonLog: self.maxDepth = DeepbluTools().getDepth(jsonLog['diveMaxDepth'], self.airPressure, self.waterType)
		if '_DiveGear' in jsonLog: self.diveGear = diveGear(jsonLog['_DiveGear'])
		self.diveProfile = diveProfile(jsonLog['_diveProfile'], self)
		if 'divespot' in jsonLog: self.diveSpot = diveSpot(jsonLog['divespot'])
		if '_DiveCondition' in jsonLog:
			if 'visibility' in jsonLog['_DiveCondition']: self.visibility = jsonLog['_DiveCondition']['visibility']
			if 'averageDepth' in jsonLog['_DiveCondition']: self.averageDepth = DeepbluTools().getDepth(jsonLog['_DiveCondition']['averageDepth'], self.airPressure, self.waterType)

class diveGear(object):
	def __init__(self, diveGear):
		if 'airMix' in diveGear: self.airMix = diveGear['airMix']
		if 'endBar' in diveGear: self.endBar = diveGear['endBar']
		if 'startedBar' in diveGear: self.startBar = diveGear['startedBar']
		if 'suitType' in diveGear: self.suitType = diveGear['suitType']

class diveProfile(object):
	def __init__(self, diveprofile, root):
		self.time = 0
		self.waypoints = []
		for waypoint in diveprofile:
			self.waypoints.append(wayPoint(waypoint, root, self))

class wayPoint(object):
	def __init__(self, waypoint, root, parent):
		airPressure = root.airPressure
		waterType = root.waterType
		depth = DeepbluTools().getDepth(waypoint['pressure'], airPressure, waterType)

		if 'time' in waypoint and waypoint['time']:
			parent.time = waypoint['time']
		else:
			parent.time += 20
		
		self.depth = depth
		self.time = parent.time
		if 'temperature' in waypoint:
			self.temp = DeepbluTools().convertTemp(waypoint['temperature'])

class DeepbluTools:
	# Gets depth in metres. Formula looks wrong but it
	# is actually compensating for values incorrectly
	# stored by Deepblu

	def getDepth(self, press, airpress, fresh):
		if not press: return -1
		r = 1.025 if fresh and fresh == 1 else 1.0

		if not airpress: airpress = 1000
		
		if airpress and airpress in range(400, 1100):
			return ((press-airpress) / r / 100)

	# Deepblu reports temperature values in decicelsius
	# Let's store them in Kelvin
	def convertTemp(self, decicelsius):
		return (decicelsius / 10) + 273.15 # Decicelsius to Kelvin

class diveSpot(object):
	def __init__(self, divespot):
		if '_id' in divespot: self.id = 'deepblu_ds_' + divespot['_id']
		if 'divespot' in divespot: self.name = divespot['divespot']
		if 'gpsLocation' in divespot:
			if 'lat' in divespot['gpsLocation']: self.lat = divespot['gpsLocation']['lat']
			if 'lng' in divespot['gpsLocation']: self.lon = divespot['gpsLocation']['lng']

class UDDFWriter(object):
	def __init__(self, logBook):
		generator = {
			'name': 'Deepblu Backup Tool',
			'creator': 'Sander Van de Moortel',
			'contact': 'https://github.com/bluppfisk/deepblu-tools',
			'version': '0.2',
			'date': str(datetime.now())
		}

		self.data = {
			'logs': logBook.logs,
			'diveSpots': logBook.diveSpots,
			'generator': generator
		}

	def toFile(self, filename):
		print("Writing to '" + filename + "'")
		f = open(filename, 'w')
		f.write(self.output())
		f.close()
		print("Done!")

	def output(self):
		templateLoader = jinja2.FileSystemLoader(searchpath="./")
		templateEnv = jinja2.Environment(loader=templateLoader)
		TEMPLATE_FILE = "template.uddf"
		template = templateEnv.get_template(TEMPLATE_FILE)
		return template.render(self.data)

with open('login','r') as loginfile:
    logindata = eval(loginfile.read())

deepbluUser = DeepbluUser().login(logindata['user'], logindata['pass'])
deepbluLogBook = Deepblu().loadDivesFromAPI(deepbluUser)
UDDFWriter(deepbluLogBook).toFile('backup.uddf')