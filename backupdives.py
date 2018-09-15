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
#        

import sys, requests, json, time, jinja2, hashlib, argparse
from datetime import datetime
from xml.sax.saxutils import escape

CHUNKSIZE = 100 # Don't load everything at once
VERSION = '0.9.6'

DEEPBLU_API = "https://prodcdn.tritondive.co/apis/"
DEEPBLU_LOGIN_API = DEEPBLU_API + "user/v0/login"
# DEEPBLU_DIVES_API = DEEPBLU_API + "discover/v0/post/search?postType=divelog&userId=" # Old Deepblu posts API
DEEPBLU_DIVES_API = DEEPBLU_API + "discover/v0/post/{}/diveLog?limit={}&skip={}"
DEEPBLU_DRAFT_DIVES_API = DEEPBLU_API + "divelog/v0/getRawLogs?hide=0&type=1&limit={}&skip={}"
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
	def getAllLogsFromAPI(self, deepbluUser, drafts, max_posts=None):
		print("Getting published logs")
		publishedPosts =  self.loadDivesFromAPI(deepbluUser, type='published')
		draftPosts = []

		if drafts:
			if deepbluUser.loggedIn:
				print("Getting draft logs for logged in user")
				draftPosts = self.loadDivesFromAPI(deepbluUser, type='draft')
			else:
				print("Cannot get drafts if user is not logged in")

		return DeepbluLogBook(publishedPosts + draftPosts, deepbluUser, max_posts)

	def loadDivesFromAPI(self, deepbluUser, type):
		headers = {
			"content-type": "application/json; charset=utf-8",
			"authorization": deepbluUser.authCode,
			"accept-language": "en"
		}

		skip = 0
		posts = []
		result_index_name = 'posts' if type == 'published' else 'logs'

		print("Loading first {} {} logs from Deepblu API...".format(CHUNKSIZE, type))

		###
		# This will load chunks from the API until there are no more logs or
		# until the API call fails, in which case we'll set skip to -1
		# 
		while skip >= 0:
			if type == "published":
				url = DEEPBLU_DIVES_API.format(deepbluUser.userId, CHUNKSIZE, skip)
			else:
				url = DEEPBLU_DRAFT_DIVES_API.format(CHUNKSIZE, skip)
			res = requests.get(url, headers=headers)
			response = json.loads(res.text)
			if response.get('statusCode') == 200:  # result!
				if len(response.get('result', {}).get(result_index_name)) > 0:
					if skip > 0:
						print("Loading next {} {} logs...".format(CHUNKSIZE, type))

					new_posts = response.get('result', {}).get(result_index_name)
					if type == 'published':
						posts += new_posts
					else:
						for post in new_posts:
							new_post = {'diveLog': post, 'medias': {}}
							posts.append(new_post)

					skip += CHUNKSIZE # next chunk
				else:
					# we're done here
					print("Found all the {} logs!".format(type))
					skip = -1

			else:
				# API call failed
				if deepbluUser.loggedIn:
					print(str(response.get('statusCode')) + ",API Error. God knows what happened at Deepblu.")
				else:
					print(str(response.get('statusCode')) + ",Incorrect user + password combination or user id.")
				exit()
				skip = -1
				return False

		return posts

###
# A logbook containing all logs as well summaries for
# persons, equipment, gas definitions, media and divespots
# that may be referenced in the individual logs
# 
class DeepbluLogBook(object):
	def __init__(self, posts, deepbluUser, max_posts):
		print ("Parse all the things!")
		self.logs = []
		self.owner = deepbluUser


		for post in posts:
			if max_posts is not None and len(self.logs) >= max_posts:  # max posts reached; stop appending
				break

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
		self._start_epoch = None
		self.id = 'deepblu_dl_' + jsonLog.get('_id')
		self.diveDate = datetime.strptime(jsonLog.get('diveDTRaw'), "%Y,%m,%d,%H,%M,%S")
		self.airPressure = jsonLog.get('airPressure', 1000)
		self.waterType = jsonLog.get('waterType', 0)
		self.notes = escape(jsonLog.get('notes', ''))
		self.diveDuration = jsonLog.get('diveDuration', '')
		self.minTemp = DeepbluTools.convertTemp(jsonLog.get('diveMinTemperature', None))
		self.maxDepth = DeepbluTools.getDepth(jsonLog.get('diveMaxDepth', None), self.airPressure, self.waterType)
		self.diveGear = diveGear(jsonLog.get('_DiveGear', {}))
		# UDDF scheme prescribes for dive mode (i.e. apnea or scuba) to be included at waypoint level
		# as it is technically possible to change diving mode while diving
		# 'apnoe' is the German keyword used in UDDF < 3.2.2; using this for compatibility reasons
		self.diveMode = 'apnoe' if jsonLog.get('diveType') == 'Free' else 'opencircuit'
		self.diveProfile = diveProfile(jsonLog.get('_diveProfile'), self)
		self.diveSpot = diveSpot(jsonLog.get('divespot', {}))
		self.visibility = jsonLog.get('_DiveCondition', {}).get('visibility', None)
		self.airTemperature = jsonLog.get('_DiveCondition', {}).get('avgTemperature', None)
		if self.airTemperature:
			# for some obscure reason, this is not in decicelsius like elsewhere
			self.airTemperature = DeepbluTools.convertTemp(self.airTemperature*10)
		self.averageDepth = DeepbluTools.getDepth(jsonLog.get('_DiveCondition', {}).get('averageDepth', None), self.airPressure, self.waterType)
		
		self.buddies = []
		for buddy in jsonLog.get('diveBuddiesObj', {}):
			self.buddies.append(Diver(buddy))

		self.media = []
		for medium in media:
			self.media.append(Medium(medium))

###
# This is a diver (person). For now this is only buddies.
# Owner should probably extend or implement this class
# But since we're only setting properties and this is Python,
# it doesn't really matter?
# 
class Diver(object):
	def __init__(self, diver):
		self.id = diver.get('diveBuddyUserId')
		self.name = escape(diver.get('diveBuddyUserName'))

###
# Singular of media, i.c. videos and photos
# This program does not download your videos
# and photos (yet), but it does keep a reference
# 
class Medium(object):
	def __init__(self, medium):
		self.id = 'deepblu_md_' + medium.get('_id')
		self.url = medium.get('url')
		self.caption = escape(medium.get('caption', ''))
		timestamp = medium.get('timestamp')
		if timestamp:
			self.datetime = datetime.fromtimestamp(timestamp).isoformat()
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
		self.tankVolume = diveGear.get('airTank', {}).get('volume')
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
		self.brand = escape(str(brandModel.get('brand')))
		self.model = escape(str(brandModel.get('officialModel')))
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
# 'root' refers to dive log
# 
class diveProfile(object):
	def __init__(self, diveprofile, root):
		self.time = 0  # keeps track of time for waypoints
		self.waypoints = []
		for waypoint in diveprofile:
			self.waypoints.append(wayPoint(waypoint, root, self))

###
# wayPoint contains depth, temperature and time
# think of it as a dive computer sample point
# 'parent' refers to diveProfile; 'root' to DeepbluLog
# 
class wayPoint(object):
	def __init__(self, waypoint, root, parent):
		# convert from millibar to water depth
		airPressure = root.airPressure
		waterType = root.waterType
		depth = DeepbluTools.getDepth(waypoint.get('pressure'), airPressure, waterType)

		# A quirk of Deepblu is that, for some logs, it saves the dive time of waypoints
		# in Unix epoch time. This is why we keep track of the first waypoint time
		# and subtract it later from each following waypoint's time
		if root._start_epoch == None:
			root._start_epoch = waypoint.get('time') if waypoint.get('time') else 0
		# For some logs, Deepblu does not save time correctly, however Deepblu
		# always keeps a waypoint every 20 seconds. So if no time is set, add 20 s
		parent.time = waypoint.get('time') if waypoint.get('time') else parent.time + 20
		parent.time -= root._start_epoch  # subtract 0 or unix time from each waypoint
		
		self.depth = depth
		self.time = parent.time
		self.diveMode = root.diveMode # 'apnoe' for freediving; 'opencircuit' for scuba
		self.temp = DeepbluTools.convertTemp(waypoint.get('temperature')) # convert to Kelvin

###
# Toolbox class, does not get instantiated and therefore
# does not pass self as an argument to its functions
# 
class DeepbluTools:
	# Gets depth in metres. Formula looks wrong but it
	# is actually compensating for values incorrectly
	# stored by Deepblu
	@staticmethod
	def getDepth(press, airpress, fresh):
		if not press: return None
		r = 1.025 if fresh and fresh == 1 else 1.0

		if not airpress: airpress = 1000
		
		if airpress and airpress in range(400, 1100):
			return ((press-airpress) / r / 100)

	# Deepblu reports temperature values in decicelsius
	# Let's store them in Kelvin
	@staticmethod
	def convertTemp(decicelsius):
		if decicelsius == None:
			return None

		return (decicelsius / 10) + 273.15 # Decicelsius to Kelvin

class diveSpot(object):
	def __init__(self, divespot):
		self.id = 'deepblu_ds_' + str(divespot.get('_id'))
		self.name = escape(str(divespot.get('divespot')))
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
			'version': VERSION,
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
		filename = './done/' + filename
		print("Writing to '" + filename + "'")
		f = open(filename, 'wb')
		f.write(self.output().encode('UTF-8'))
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
print('##############################################')
print('# Deepblu Backup Tool v' + VERSION + '                 #')
print('# https://github.com/bluppfisk/deepblu-tools #')
print('##############################################')

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d', '--with-drafts', help='Also download draft logs', action='store_true')
parser.add_argument('-m', '--max', help='Max number of logs to parse', type=int, required=False)
parser.add_argument('-u', '--username', help='Specify username', action='store', required=True)
parser.add_argument('-p', '--password', help='Specify password', action='store', default='', required=False)
args = parser.parse_args()

user = args.username
pwd = args.password
max_posts = args.max
drafts = args.with_drafts

targetfile = 'backup_' + hashlib.sha1((user+pwd).encode('UTF-8')).hexdigest()[0:10] + '.uddf'

deepbluUser = DeepbluUser().login(user, pwd)  # login user

if not deepbluUser.loggedIn:  # not logged in, get data from API without logging in
	print("Attempting to access API without logging in... (experimental)")  # may fail if they ever restrict access

deepbluLogBook = Deepblu().getAllLogsFromAPI(deepbluUser, drafts=drafts, max_posts=max_posts)  # call API and get data

if deepbluLogBook:
	UDDFWriter(deepbluLogBook).toFile(targetfile)  # print to templating engine
	print("0,"+targetfile)  # output for caller
else:
	print("1,Unexpected error occurred. Useful info, huh!")
