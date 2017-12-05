#! /usr/bin/env python3
###
# Deepblu Backup Tool
# by Sander Van de Moortel
# 
# https://github.com/bluppfisk/deepblu-tools
# 
# Connects to Deepblu and backs up dives in UDDF format
# See http://uddf.org for more information on the format
# 
# Requirements: Python >= 3.3, requests and jinja2 packages
# Usage: - fill in your login details in the separate login file
#        - then run this script: python3 backupdives.py
#        - find the file called backup.uddf in the same folder
#        

import sys, requests, json, time, jinja2, hashlib
from datetime import datetime

CHUNKSIZE = 20 # Don't load everything at once

DEEPBLU_API = "https://prodcdn.tritondive.co/apis/"
DEEPBLU_LOGIN_API = DEEPBLU_API + "user/v0/login"
DEEPBLU_DIVES_API = DEEPBLU_API + "discover/v0/post/search?postType=divelog&userId="
DEEPBLU_PROFILE_API = DEEPBLU_API + "user/v0/profile/"

###
# DeepbluUser class to log in a user into Deepblu
# 
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

		if response.get('statusCode') == 200:
			userData = response.get('result', {}).get('userInfo', {})
			self.setDataFromJSON(userData)

			self.authCode = response.get('result', {}).get('accessToken')
			self.loggedIn = True
			print("Logged in as " + email + '!')
		else:
			print("Could not log in " + email + ", error code: " + str(response.get('statusCode')))
			self.loggedIn = False
			self.authCode = None
			self.userId = email

		return self

	###
	# Populate DeepbluUser properties with JSON data returned from API
	# 
	def setDataFromJSON(self, userData):
		self.userId = userData.get('ownerId')
		self.firstName = userData.get('firstName')
		self.lastName = userData.get('lastName')
		self.email = userData.get('email')
		birthday = userData.get('Birthday', {})

		if birthday:
			self.birthday = datetime(
				int(birthday.get('Year')),
				int(birthday.get('Month')),
				int(birthday.get('Day'))
			)

###
# Deepblu API class
# Should probably be abstracted for use by other tools
# 
class Deepblu(object):

	###
	# Load divelogs from Deepblu API
	# 
	def loadDivesFromAPI(self, deepbluUser):
		headers = {
			"content-type": "application/json; charset=utf-8",
			"authorization": deepbluUser.authCode,
			"accept-language": "en"
		}

		skip = 0
		posts = []

		print("Loading first " + str(CHUNKSIZE) + " logs from Deepblu API...")

		###
		# This will load chunks from the API until there are no more logs or
		# until the API call fails, in which case we'll set skip to -1
		# 
		while skip >= 0:
			res = requests.get(DEEPBLU_DIVES_API + deepbluUser.userId + "&limit=" + str(CHUNKSIZE) + "&skip=" + str(skip), headers=headers)
			response = json.loads(res.text)
			if response.get('statusCode') == 200: # result!
				if len(response.get('result', {}).get('posts')) > 0:
					if skip > 0:
						print("Loading next " + str(CHUNKSIZE) + " logs...")

					posts += response.get('result', {}).get('posts')
					skip += CHUNKSIZE # next chunk
				else:
					# we're done here
					print("Found all the logs!")
					skip = -1
			else:
				# API call failed
				print("Error obtaining dive logs, error code: " + str(response.get('statusCode')))
				skip = -1
				return False
			
		return DeepbluLogBook(posts, deepbluUser)

###
# A logbook containing all logs as well summaries for
# persons, equipment, gas definitions, media and divespots
# that may be referenced in the individual logs
# 
class DeepbluLogBook(object):
	def __init__(self, posts, deepbluUser):
		print ("Parse all the things!")
		self.logs = []
		self.owner = deepbluUser

		for post in posts:
			self.logs.append(DeepbluLog(post.get('diveLog'), post.get('medias')))

		self.getUniqueMedia()
		self.getUniqueDiveSpots()
		self.getUniqueGasDefinitions()
		self.getUniqueBuddies()
		self.getUniqueEquipment()

	###
	# Below functions eliminate duplicates from the summaries
	# of equipment, buddies, divespots, etc
	# 
	def getUniqueEquipment(self):
		self.equipment = []
		for log in self.logs:
			for item in log.diveGear.equipment:
				if not self.findEquipmentById(item.id):
					self.equipment.append(item)

	def getUniqueBuddies(self):
		self.buddies = []
		for log in self.logs:
			for buddy in log.buddies:
				if not self.findBuddyById(buddy.id):
					self.buddies.append(buddy)

	def getUniqueDiveSpots(self):
		self.diveSpots = []
		for log in self.logs:
			if not self.findDiveSpotById(log.diveSpot.id):
				self.diveSpots.append(log.diveSpot)

	def getUniqueGasDefinitions(self):
		self.gasDefinitions = []
		for log in self.logs:
			if hasattr(log.diveGear, 'gasDefinition'):
				if hasattr(log.diveGear.gasDefinition, 'id'):
					if not self.findGasDefinitionById(log.diveGear.gasDefinition.id):
						self.gasDefinitions.append(log.diveGear.gasDefinition)

	def getUniqueMedia(self):
		self.media = []
		for log in self.logs:
			for medium in log.media:
				if not self.findMediumById(medium.id):
					self.media.append(medium)

	def findDiveSpotById(self, diveSpotId):
		for diveSpot in self.diveSpots:
			if diveSpotId == diveSpot.id:
				return diveSpot

		return False

	def findGasDefinitionById(self, gasDefinitionId):
		for gasDefinition in self.gasDefinitions:
			if gasDefinitionId == gasDefinition.id:
				return gasDefinition

		return False

	def findMediumById(self, mediumId):
		for medium in self.media:
			if mediumId == medium.id:
				return medium

		return False

	def findEquipmentById(self, equipmentId):
		for item in self.equipment:
			if equipmentId == item.id:
				return item

		return False

	def findBuddyById(self, buddyId):
		for buddy in self.buddies:
			if buddyId == buddy.id:
				return buddy

		return False

###
# The big Log object with all its properties
#
class DeepbluLog(object):
	def __init__(self, jsonLog, media):
		self.id = 'deepblu_dl_' + jsonLog.get('divelogId')
		self.diveDate = datetime.strptime(jsonLog.get('diveDTRaw'), "%Y,%m,%d,%H,%M,%S")
		self.airPressure = jsonLog.get('airPressure', 1000)
		self.waterType = jsonLog.get('waterType', 0)
		self.notes = jsonLog.get('notes', '')
		self.diveDuration = jsonLog.get('diveDuration', '')
		self.minTemp = DeepbluTools.convertTemp(jsonLog.get('diveMinTemperature', None))
		self.maxDepth = DeepbluTools.getDepth(jsonLog.get('diveMaxDepth', None), self.airPressure, self.waterType)
		self.diveGear = diveGear(jsonLog.get('_DiveGear', {}))
		self.diveProfile = diveProfile(jsonLog.get('_diveProfile'), self)
		self.diveSpot = diveSpot(jsonLog.get('divespot'))
		self.visibility = jsonLog.get('_DiveCondition', {}).get('visibility', None)
		self.averageDepth = DeepbluTools.getDepth(jsonLog.get('_DiveCondition', {}).get('averageDepth', None), self.airPressure, self.waterType)
		
		self.buddies = []
		for buddy in jsonLog.get('diveBuddiesObj', {}):
			self.buddies.append(Diver(buddy))

		self.media = []
		for medium in media:
			self.media.append(Medium(medium))

###
# This is a diver (person). For now this is only buddies
# Owner should probably extend or implement this class
# But since we're only setting properties and this is Python,
# it doesn't really matter?
# 
class Diver(object):
	def __init__(self, diver):
		self.id = diver.get('diveBuddyUserId')
		self.name = diver.get('diveBuddyUserName')

###
# Singular of media, i.c. videos and photos
# This program does not download your videos
# and photos (yet), but it does keep a reference
# 
class Medium(object):
	def __init__(self, medium):
		self.id = 'deepblu_md_' + medium.get('_id')
		self.url = medium.get('url')
		self.caption = medium.get('caption', '')
		self.datetime = datetime.fromtimestamp(medium.get('timestamp')).isoformat()
		if medium.get('type') == "Video":
			self.type = 'video'
		else:
			self.type = 'image'

###
# All gear, including list of equipment
# Clumsy class, really. My bad
# 
class diveGear(object):
	def __init__(self, diveGear):
		self.gasDefinition = gasDefinition(diveGear.get('airMix'))
		self.tank = diveGear.get('airTank', {}).get('volume')
		if diveGear.get('endBar'):
			self.endBar = int(diveGear.get('endBar')) * 10**5
		if diveGear.get('startedBar'):
			self.startBar = int(diveGear.get('startedBar')) * 10**5
		self.suit = diveGear.get('suitType')
		self.equipment = []
		for divecomputer in diveGear.get('diveComputer', {}):
			self.equipment.append(Equipment('divecomputer', divecomputer))

###
# Every piece of equipment is of a certain type, and has a manufacturer and model
# 
class Equipment(object):
	def __init__(self, kind, brandModel):
		self.type = kind
		self.brand = brandModel.get('brand')
		self.model = brandModel.get('officialModel')
		self.id = 'eq_' + hashlib.sha1((self.brand + self.model).encode('UTF-8')).hexdigest()[0:8]

###
# Deepblu only saves nitrogen and oxygen values for air mixes
# 
class gasDefinition(object):
	def __init__(self, airmix):
		if not airmix:
			return None

		self.o2 = airmix / 100
		self.n2 = (100 - airmix) / 100
		self.id = "mix" + str(airmix)
		self.name = str(airmix) + "/" + str(100 - airmix)

###
# diveProfile consists of wayPoints
# 
class diveProfile(object):
	def __init__(self, diveprofile, root):
		self.time = 0 # keeps track of time for waypoints
		self.waypoints = []
		for waypoint in diveprofile:
			self.waypoints.append(wayPoint(waypoint, root, self))
###
# wayPoint contains depth, temperature and time
# think of it as a dive computer sample point
# 
class wayPoint(object):
	def __init__(self, waypoint, root, parent):
		# convert from millibar to water depth
		airPressure = root.airPressure
		waterType = root.waterType
		depth = DeepbluTools.getDepth(waypoint.get('pressure'), airPressure, waterType)

		# For some logs, Deepblu does not save time correctly, however Deepblu
		# always keeps a waypoint every 20 seconds. So if no time is set, add 20 s
		parent.time = waypoint.get('time') if waypoint.get('time') else parent.time + 20
		
		self.depth = depth
		self.time = parent.time
		self.temp = DeepbluTools.convertTemp(waypoint.get('temperature')) # convert to Kelvin

# Toolbox class, does not get instantiated and therefore
# does not pass self as an argument to its functions
class DeepbluTools:
	# Gets depth in metres. Formula looks wrong but it
	# is actually compensating for values incorrectly
	# stored by Deepblu
	def getDepth(press, airpress, fresh):
		if not press: return None
		r = 1.025 if fresh and fresh == 1 else 1.0

		if not airpress: airpress = 1000
		
		if airpress and airpress in range(400, 1100):
			return ((press-airpress) / r / 100)

	# Deepblu reports temperature values in decicelsius
	# Let's store them in Kelvin
	def convertTemp(decicelsius):
		if decicelsius == None:
			return None

		return (decicelsius / 10) + 273.15 # Decicelsius to Kelvin

class diveSpot(object):
	def __init__(self, divespot):
		self.id = 'deepblu_ds_' + divespot.get('_id')
		self.name = divespot.get('divespot')
		self.lat = divespot.get('gpsLocation', {}).get('lat')
		self.lon = divespot.get('gpsLocation', {}).get('lng')

###
# Pushes the data to Jinja2 templating engine
# which will create the final UDDF format file
#  
class UDDFWriter(object):
	def __init__(self, logBook):
		# Generator information
		generator = {
			'name': 'Deepblu Backup Tool',
			'creator': 'Sander Van de Moortel',
			'contact': 'https://github.com/bluppfisk/deepblu-tools',
			'version': '0.5',
			'date': str(datetime.now())
		}

		# Data for templating engine
		self.data = {
			'logs': logBook.logs,
			'divers': {
				'owner': logBook.owner,
				'buddies': logBook.buddies
			},
			'diveSpots': logBook.diveSpots,
			'gasDefinitions': logBook.gasDefinitions,
			'media': logBook.media,
			'generator': generator
		}

	# Takes templating engine output and writes to file
	def toFile(self, filename):
		print("Writing to '" + filename + "'")
		f = open(filename, 'w')
		f.write('./done' + self.output())
		f.close()
		print("Done!")

	# Invokes templating engine and feeds it data
	def output(self):
		templateLoader = jinja2.FileSystemLoader(searchpath="./")
		templateEnv = jinja2.Environment(loader=templateLoader)
		TEMPLATE_FILE = "template.uddf"
		template = templateEnv.get_template(TEMPLATE_FILE)
		return template.render(self.data)


###
# This part controls the flow of the program
# 
if len(sys.argv) > 1: # shell arguments given
	user = str(sys.argv[1])
	if len(sys.argv) == 3: # ooh, a password too, we can log in
		pwd = str(sys.argv[2])
	else: # no password; we'll try accessing the API without
		pwd = None

	targetfile = 'backup_' + hashlib.sha1(user.encode('UTF-8')).hexdigest()[0:10] + '.uddf'

else: # no shell arguments, read login data from file
	with open('login','r') as loginfile:
	    logindata = eval(loginfile.read())
	    user = logindata.get('user')
	    pwd = logindata.get('pwd')
	    targetfile = 'backup.uddf'

deepbluUser = DeepbluUser().login(user, pwd) # login user

if not deepbluUser.loggedIn: # not logged in, get data from API without logging in
	print("Attempting to access API without logging in... (experimental)") # may fail if they ever restrict access

deepbluLogBook = Deepblu().loadDivesFromAPI(deepbluUser) # call API and get data
if deepbluLogBook:
	UDDFWriter(deepbluLogBook).toFile(targetfile) # print to templating engine

print(targetfile) # output for caller