import requests, json, time, jinja2

DEEPBLUAPI = "https://prodcdn.tritondive.co/apis/discover/v0/post/search?postType=divelog&userId=5823faa12e577e38554e8e13&limit=20&skip=0"

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
		res = requests.post(DEEPBLU_LOGIN_API, data=json.dumps(data), headers=headers)
		response = json.loads(res.text)

		if response['statusCode'] == 200:
			self.userId = response['result']['userInfo']['ownerId']
			self.authCode = response['result']['accessToken']
			# print("Obtained token for " + email + '!')
		else:
			print("Account " + email + " could not log in, error code: " + str(response['statusCode']))
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
		
		res = requests.get(DEEPBLU_DIVES_API + deepbluUser.userId + "&limit=" + str(CHUNKSIZE) + "&skip=" + str(skip), headers=headers)
		response = json.loads(res.text)

		if response['statusCode'] == 200:
			return DeepbluLogBook(response['result']['posts'])
		else:
			print("Error obtaining dive logs, error code: " + str(response['statusCode']))

class DeepbluLogBook(object):
	def __init__(self, logs):
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

	def output(self):
		print("Here is the love: \n")
		print(self.logBook)


class DeepbluLog(object):
	def __init__(self, jsonLog):
		self.id = 'deepblu_dl_' + jsonLog['divelogId']
		self.diveDate = jsonLog['diveDT']
		self.airPressure = jsonLog['airPressure']
		self.waterType = jsonLog['waterType']
		self.diveDuration = jsonLog['diveDuration']
		self.minTemp = (jsonLog['diveMinTemperature']/10) + 273.15
		self.averageDepth = DeepbluTools().getDepth(jsonLog['_DiveCondition']['averageDepth'], self.airPressure, self.waterType)
		self.maxDepth = DeepbluTools().getDepth(jsonLog['diveMaxDepth'], self.airPressure, self.waterType)
		# self.diveGear = diveGear(jsonLog['diveGear'])
		self.diveProfile = diveProfile(jsonLog['_diveProfile'], self)
		self.diveSpot = diveSpot(jsonLog['divespot'])

class diveProfile(object):
	def __init__(self, diveprofile, deepbluLog):
		airPressure = deepbluLog.airPressure
		waterType = deepbluLog.waterType
		self.waypoints = []

		time = 0
		for waypoint in diveprofile:
			depth = DeepbluTools().getDepth(waypoint['pressure'], airPressure, waterType)
			if 'time' in waypoint and waypoint['time']:
				time = waypoint['time']
			else:
				time += 20

			self.waypoints.append(wayPoint(depth, time))

class wayPoint(object):
	def __init__(self, depth, time):
		self.depth = depth
		self.time = time

class DeepbluTools:
	def getDepth(self, press, airpress, fresh):
		if not press: return -1
		r = 1.025 if fresh and fresh == 1 else 1.0

		if not airpress: airpress = 1000
		
		if airpress and airpress in range(400, 1100):
			return ((press-airpress) / r / 100)

class diveSpot(object):
	def __init__(self, divespot):
		self.name = divespot['divespot']
		self.lat = divespot['gpsLocation']['lat']
		self.lon = divespot['gpsLocation']['lng']
		self.id = 'deepblu_ds_' + divespot['_id']


class UDDFWriter(object):
	def __init__(self, logBook):
		generator = {
			'name': 'Deepblu Backup Tool',
			'creator': 'Sander Van de Moortel',
			'contact': 'https://github.com/bluppfisk/deepblu-tools',
			'version': '0.1',
			'date': '3 December 2017'
		}

		self.data = {
			'logs': logBook.logs,
			'diveSpots': logBook.diveSpots,
			'generator': generator
		}

	def output(self):
		templateLoader = jinja2.FileSystemLoader(searchpath="./")
		templateEnv = jinja2.Environment(loader=templateLoader)
		TEMPLATE_FILE = "template.uddf"
		template = templateEnv.get_template(TEMPLATE_FILE)
		print(template.render(self.data))

with open('login','r') as loginfile:
    logindata = eval(loginfile.read())

deepbluUser = DeepbluUser().login(logindata['user'], logindata['pass'])
deepbluLogBook = Deepblu().loadDivesFromAPI(deepbluUser)
UDDFWriter(deepbluLogBook).output()

					 # "diveLog": {
      #     "_DiveCondition": {
      #       "averageDepth": 2544.0785714285716,
      #       "minWaterTemperature": 277,
      #       "weather": -1
      #     },
      #     "_DiveGear": {
      #       "BCD": [],
      #       "airMix": 21,
      #       "camera": [],
      #       "cameraHousing": [],
      #       "cameraLens": [],
      #       "cameraLight": [],
      #       "cameraStrobe": [],
      #       "diveComputer": [
      #         {
      #           "_id": "00000-00000",
      #           "brand": "Deepblu",
      #           "btName": "COSMIQ",
      #           "officialModel": "COSMIQ"
      #         }
      #       ],
      #       "fins": [],
      #       "lightTorch": [],
      #       "regulator": {
      #         "firstStage": [],
      #         "secondStage": []
      #       }
      #     },
      #     "_diveProfile": [
      #       {
      #         "id": "0",
      #         "pressure": 1349,
      #         "temperature": 290,
      #         "time": 20
      #       },
