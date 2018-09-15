# Formats logbook data in UDDF format and writes to file or outputs to screen

import jinja2
from datetime import datetime


class UDDFWriter:
	def __init__(self, logBook, generator):
		self.data = {
			'date': str(datetime.now()),
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

	# Invokes templating engine and feeds it data
	def output(self):
		templateLoader = jinja2.FileSystemLoader(searchpath="./")
		templateEnv = jinja2.Environment(loader=templateLoader)
		TEMPLATE_FILE = "template.uddf"
		template = templateEnv.get_template(TEMPLATE_FILE)
		return template.render(self.data)
