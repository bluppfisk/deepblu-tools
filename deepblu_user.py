# Deepblu User

import requests, json
from datetime import datetime


class DeepbluUser:
	def __init__(self):
		self.logged_in = False
		self.auth_code = None

	# Populate DeepbluUser properties with JSON data returned from API
	def set_data_from_json(self, user_data):
		self.user_id = user_data.get('ownerId')
		self.first_name = user_data.get('firstName')
		self.last_name = user_data.get('lastName')
		self.email = user_data.get('email')
		birthday = user_data.get('Birthday', {})

		if birthday:
			self.birthday = datetime(
				int(birthday.get('Year')),
				int(birthday.get('Month')),
				int(birthday.get('Day'))
			)
