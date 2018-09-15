# Unit calculation methods

class DeepbluTools:
	# Gets depth in metres. Formula looks wrong but it is actually
	# compensating for values incorrectly stored by Deepblu
	@staticmethod
	def getDepth(press, airpress, fresh):
		if not press: return None
		r = 1.025 if fresh and fresh == 1 else 1.0

		if not airpress: airpress = 1000
		
		if airpress and airpress in range(400, 1100):
			return ((press-airpress) / r / 100)

	# Deepblu reports temperature values in decicelsius
	# UDDF expects Kelvin
	@staticmethod
	def convertTemp(decicelsius):
		if decicelsius == None:
			return None

		return (decicelsius / 10) + 273.15  # Decicelsius to Kelvin