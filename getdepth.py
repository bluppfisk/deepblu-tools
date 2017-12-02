# function getDepth(pressure, airpressure, watertype=0) {
# 	if (!pressure) return -1;
# 	var r = watertype && 1 === watertype ? 1.025 : 1;
# 	return airpressure && airpressure > 400 && airpressure < 1100 || (airpressure = 1e3), (pressure - airpressure) / r / 100;
# }

class DeepbluTools:
	def getDepth(self, press, airpress, fresh):
		if not press: return -1
		r = 1.025 if fresh and fresh == 1 else 1.0

		if not airpress: airpress = 1000
		
		if airpress and airpress in range(400, 1100):
			return ((press-airpress) / r / 100)


print DeepbluTools().getDepth(3584, 1001, 0)