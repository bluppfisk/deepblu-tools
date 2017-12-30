# deepblu-tools
Deepblu API tools

A set of tools to get the most out of [Deepblu](https://deepblu.com).

## Deepblu Backup Tool - backupdives.py
Retrieves dive logs from Deepblu and exports them in [Universal Dive Data Format](http://uddf.org) (UDDF), which can be imported into other applications that support it, including [Subsurface Divelog](https://subsurface-divelog.org/).

![Deepblu logs imported into Subsurface](/images/imported_into_subsurface.jpg)

### Requirements
- Make sure you have Python 3 and pip3 installed
- run `pip3 install requests jinja2` to install the required dependencies

### Usage
- run `python3 backupdives.py email password`
- or run `python3 backupdives.py userId` or
- or fill in your login details in the separate **login** file, then run this script: `python3 backupdives.py`
- or use the [Deepblu Backup Tool web service](http://worldofnonging.com/deepblu-tools/index.php)
- find the newly generated backup file in the `done` folder

### Tracked data
- Dive type: Freediving (apnea) or Scuba (open circuit)
- Dive profile: Deepblu provides a waypoint with temperature and depth every 20 seconds
- Date and time, visibility, average depth, maximum depth, minimum temperature, dive duration
- Media: url, captions and timestamps of video and images
- Tank: volume, gas, pressure at start and end
- Dive computer brand and model
- Diver details
- Buddies
- Divespot: name, latitude and longitude
- Notes

### Known issues
- Not all data is currently being backed up (some equipment data isn't). I may add more items in the future.

## Deepblu Autoliker - autoliker.py
Logs you in with a set of accounts defined in **LOGINS** and automatically likes every post, beginning with the most recent one, until **MAX_LIKES** is reached or an earlier like is found.

## Deepblu Autofollow - autofollow.js
Console JS script to automatically add a series of Deepblu users in **userIds** to the following list of a logged-in account with token **authToken**.
