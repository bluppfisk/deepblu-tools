# deepblu-tools
Deepblu API tools

A set of tools to get the most out of [Deepblu](https://deepblu.com).

## backupdives.py
Retrieves dive logs from Deepblu and exports them in [Universal Dive Data Format](http://uddf.org) (UDDF), which can be imported into other applications that support it, including [Subsurface Divelog](https://subsurface-divelog.org/).

![Deepblu logs imported into Subsurface](/images/imported_into_subsurface.jpg)

### Requirements
- Make sure you have Python 3 and pip3 installed
- run `pip3 install requests jinja2` to install the required dependencies

### Usage
- fill in your login details in the separate **login** file
- then run this script: `python3 backupdives.py`
- find the newly generated file called **backup.uddf** in the same folder

## autoliker.py
Logs you in with a set of accounts defined in **LOGINS** and automatically likes every post, beginning with the most recent one, until **MAX_LIKES** is reached or an earlier like is found.

## autofollow.js
Console JS script to copy automatically add a series of Deepblu users in **userIds** to the following list of a logged-in account with token **authToken**.