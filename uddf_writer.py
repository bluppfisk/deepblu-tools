# Formats logbook data in UDDF format and writes to file or outputs to screen

import jinja2
from datetime import datetime


class UDDFWriter:
	def __init__(self, log_book, generator):
		self.data = {
			'date': str(datetime.now()),
			'logs': log_book.logs,
			'divers': {
				'owner': log_book.owner,
				'buddies': log_book.buddies
			},
			'dive_spots': log_book.dive_spots,
			'gas_definitions': log_book.gas_definitions,
			'media': log_book.media,
			'generator': generator
		}

	# Takes templating engine output and writes to file
	def to_file(self, filename):
		filename = './done/' + filename
		print("Writing to '" + filename + "'")
		f = open(filename, 'wb')
		f.write(self.output().encode('UTF-8'))
		f.close()

	# Invokes templating engine and feeds it data
	def output(self):
		template_loader = jinja2.FileSystemLoader(searchpath="./")
		template_env = jinja2.Environment(loader=template_loader)
		TEMPLATE_FILE = "template.uddf"
		template = template_env.get_template(TEMPLATE_FILE)
		return template.render(self.data)
