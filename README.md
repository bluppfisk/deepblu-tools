[![PyPI version](https://badge.fury.io/py/deepblu-tools.svg)](https://pypi.org/project/deepblu-tools/)

# deepblu-tools
Deepblu API tools

A set of tools to get the most out of [Deepblu](https://deepblu.com).

## Deepblu Backup Tool
Retrieves dive logs from Deepblu and exports them in [Universal Dive Data Format](http://uddf.org) (UDDF), which can be imported into other applications that support it, including [Subsurface Divelog](https://subsurface-divelog.org/).

[Diving Log](http://www.divinglog.de/), a commercial dive log application for Windows, based its Deepblu import tool on this project.

![Deepblu logs imported into Subsurface](/web/img/imported_into_subsurface.jpg)

### Requirements
Make sure you have Python 3 and pip3 installed

### Installation

`pip3 install deepblu-backup`

### Usage

```
Usage: deepblu-backup [OPTIONS]


Options:
  -u, --user TEXT         Deepblu username or userid
  -p, --password TEXT     Deepblu password
  -m, --max-logs INTEGER  Maximum number of logs to parse
  -d, --with-drafts       Also pull draft logs. Requires valid
                          credentials
  -o, --outfile TEXT      Write results to this file
  -f, --infile TEXT       For debugging purposes: load data 
                          from JSON file instead of API
  --help                  Show this message and exit.
```

#### Examples

- run `deepblu-backup -u userId` to backup all your public logs without personal user information (or if you have no password, e.g. if you created your account using Facebook)
- run `deepblu_backup -u email -p password` to backup all your private and public logs with personal user information
- add `--with-drafts` to include drafts (you will need to use email and password)
- add `--max-logs MAX` to limit the number of logs to the most recent number represented by *MAX*
- add `--outfile FILENAME` to write the resulting UDDF file to *FILENAME*

Alternatively, you can use the [Deepblu Backup Tool web service](http://worldofnonging.com/deepblu-tools/index.php)

in the above commands, make sure you replace `email` and `password` with the information associated with your deepblu account, and note that `userId` is not your username but the id as found in the URL when visiting your own profile at Deepblu.

### Tracked data
- Dive type: Freediving (apnea) or Scuba (open circuit)
- Dive profile: Deepblu provides a waypoint with temperature and depth every 20 seconds
- Date and time, visibility, average depth, maximum depth, minimum temperature, dive duration, air temperature
- Media: url, captions and timestamps of video and images
- Tank: volume, gas, pressure at start and end
- Dive computer brand and model
- Diver details
- Buddies
- Divespot: name, latitude and longitude
- Divebase: name
- Notes

### Known issues
- Not all data is currently being backed up (some equipment data isn't). I may add more items in the future.

## Deepblu Autoliker - extra/autoliker.py
Logs you in with a set of accounts defined in **LOGINS** and automatically likes every post, beginning with the most recent one, until **MAX_LIKES** is reached or an earlier like is found.

## Deepblu Autofollow - extra/autofollow.js
Console JS script to automatically add a series of Deepblu users in **userIds** to the following list of a logged-in account with token **authToken**.
