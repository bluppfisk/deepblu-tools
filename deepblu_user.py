# Deepblu User

import requests, json
from datetime import datetime


class DeepbluUser:
	def __init__(self):
		self.loggedIn = False
		self.authCode = None

	# Populate DeepbluUser properties with JSON data returned from API
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
