# deepblu-tools
Deepblu API tools

A set of tools to get the most out of [Deepblu](https://deepblu.com).

## Deepblu Backup Tool - backupdives.py
Retrieves dive logs from Deepblu and exports them in [Universal Dive Data Format](http://uddf.org) (UDDF), which can be imported into other applications that support it, including [Subsurface Divelog](https://subsurface-divelog.org/).

[Diving Log](http://www.divinglog.de/), a commercial dive log application for Windows, based its Deepblu import tool on this project.

![Deepblu logs imported into Subsurface](/images/imported_into_subsurface.jpg)

### Requirements
- Make sure you have Python 3 and pip3 installed
- run `pip3 install requests jinja2` to install the required dependencies (do so in a virtual environment if necessary)
- make sure `deepblu_backup.py` is executable by running `chmod u+x deepblu_backup.py` in the directory

### Usage
- run `./deepblu_backup.py -u email -p password`
- or run `./deepblu_backup.py --with-drafts -u email -p password` if you want to include your draft dives too
- or run `./deepblu_backup.py -u userId` or
- or fill in your login details in the separate **login** file, then run this script: `./deepblu_backup.py`
- or use the [Deepblu Backup Tool web service](http://worldofnonging.com/deepblu-tools/index.php)
- find the newly generated backup file in the `done` folder

in the above commands, make sure you replace `email` and `password` with the information associated with your deepblu account, and mind that `userId` is not your username but the id as found in the URL when visiting your own profile at Deepblu.

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
- Notes

### Known issues
- Not all data is currently being backed up (some equipment data isn't). I may add more items in the future.

## Deepblu Autoliker - autoliker.py
Logs you in with a set of accounts defined in **LOGINS** and automatically likes every post, beginning with the most recent one, until **MAX_LIKES** is reached or an earlier like is found.

## Deepblu Autofollow - autofollow.js
Console JS script to automatically add a series of Deepblu users in **userIds** to the following list of a logged-in account with token **authToken**.
