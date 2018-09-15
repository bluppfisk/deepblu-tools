import requests, json
from datetime import datetime

from deepblu_api import DEEPBLU_LOGIN_API


###
# DeepbluUser class to log in a user into Deepblu
# 
class DeepbluUser:
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