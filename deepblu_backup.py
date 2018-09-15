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

import hashlib, argparse

from deepblu_user import DeepbluUser
from deepblu_api import DeepbluAPI
from uddf_writer import UDDFWriter
from deepblu_logbook import DeepbluLogBook


GENERATOR = {
	'name': 'Deepblu Backup Tool',
	'version': '0.9.6',
	'creator': 'Sander Van de Moortel',
	'contact': 'https://github.com/bluppfisk/deepblu-tools'
}
		
print('##############################################')
print('# Deepblu Backup Tool v' + GENERATOR.get('version') + '                 #')
print('# ' + GENERATOR.get('contact') + ' #')
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

# generate unique enough filename for this user and password to avoid (malicious) overwriting on server
targetfile = 'backup_' + hashlib.sha1((user + pwd).encode('UTF-8')).hexdigest()[0:10] + '.uddf'

deepbluUser = DeepbluUser().login(user, pwd)  # login user

if not deepbluUser.loggedIn:  # not logged in, get data from API without logging in
	print("Attempting to access API without logging in... (experimental)")  # may fail if Deepblu ever restrict access

print("Getting published logs")
publishedPosts =  DeepbluAPI().loadDivesFromAPI(deepbluUser, type='published')
draftPosts = []

if drafts:
	if deepbluUser.loggedIn:
		print("Getting draft logs for logged in user")
		draftPosts = DeepbluAPI().loadDivesFromAPI(deepbluUser, type='draft')
	else:
		print("Cannot get drafts if user is not logged in")

deepbluLogBook = DeepbluLogBook(publishedPosts + draftPosts, deepbluUser, max_posts=max_posts)

if deepbluLogBook:
	UDDFWriter(deepbluLogBook, GENERATOR).toFile(targetfile)  # print to templating engine
	print("0," + targetfile)  # output for calling script (web service)
else:
	print("1,Unexpected error occurred. Useful info, huh!")
