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


import hashlib
import argparse

from deepblu_user import DeepbluUser
from deepblu_api import DeepbluAPI
from uddf_writer import UDDFWriter
from deepblu_logbook import DeepbluLogBook


GENERATOR = {
    "name": "Deepblu Backup Tool",
    "version": "1.0.0",
    "creator": "Sander Van de Moortel",
    "contact": "https://github.com/bluppfisk/deepblu-tools",
}

print("##############################################")
print("# Deepblu Backup Tool v" + GENERATOR.get("version") + "                 #")
print("# " + GENERATOR.get("contact") + " #")
print("##############################################")

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "-d", "--with-drafts", help="Also download draft logs", action="store_true"
)
parser.add_argument(
    "-m", "--max", help="Max number of logs to parse", type=int, required=False
)
parser.add_argument(
    "-u", "--username", help="Specify username", action="store", required=True
)
parser.add_argument(
    "-p",
    "--password",
    help="Specify password",
    action="store",
    default="",
    required=False,
)
args = parser.parse_args()

user = args.username
pwd = args.password
max_posts = args.max
drafts = args.with_drafts

# generate unique enough filename for this user and password to avoid (malicious) overwriting on server
target_file = (
    "backup_" + hashlib.sha1((user + pwd).encode("UTF-8")
                             ).hexdigest()[0:10] + ".uddf"
)

deepblu_user = DeepbluAPI.login(user, pwd)  # login user

if not deepblu_user.logged_in:  # not logged in, get data from API without logging in
    print(
        "Attempting to access API without logging in... (experimental)"
    )  # may fail if Deepblu ever restrict access

print("Getting published logs")
published_posts = DeepbluAPI.load_dives_from_api(
    deepblu_user, type="published")
draft_posts = []

if drafts:
    if deepblu_user.logged_in:
        print("Getting draft logs for logged in user")
        draft_posts = DeepbluAPI.load_dives_from_api(
            deepblu_user, type="draft")
    else:
        print("Cannot get drafts if user is not logged in")

deepblu_log_book = DeepbluLogBook(
    published_posts + draft_posts, deepblu_user, max_posts=max_posts
)

if deepblu_log_book:
    UDDFWriter(deepblu_log_book, GENERATOR).to_file(
        target_file
    )  # print to templating engine
    print("0," + target_file)  # output for calling script (web service)
else:
    print("1,Unexpected error occurred. Useful info, huh!")
