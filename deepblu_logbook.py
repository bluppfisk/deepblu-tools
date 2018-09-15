import hashlib
from datetime import datetime
from xml.sax.saxutils import escape

from deepblu_tools import DeepbluTools

###
# A logbook containing all logs as well summaries for
# persons, equipment, gas definitions, media and divespots
# that may be referenced in the individual logs
# 
class DeepbluLogBook:
    def __init__(self, posts, deepbluUser, max_posts):
        print ("Parse all the things!")
        self.logs = []
        self.owner = deepbluUser


        for post in posts:
            if max_posts is not None and len(self.logs) >= max_posts:  # max posts reached; stop appending
                break

            self.logs.append(DeepbluLog(post.get('diveLog'), post.get('medias')))

        self.getUniqueMedia()
        self.getUniqueDiveSpots()
        self.getUniqueGasDefinitions()
        self.getUniqueBuddies()
        self.getUniqueEquipment()

    def __len__(self):
        return len(self.logs)

    ###
    # Below functions eliminate duplicates from the summaries
    # of equipment, buddies, divespots, etc
    # 
    def getUniqueEquipment(self):
        self.equipment = []
        for log in self.logs:
            for item in log.diveGear.equipment:
                if not self.findEquipmentById(item.id):
                    self.equipment.append(item)

    def getUniqueBuddies(self):
        self.buddies = []
        for log in self.logs:
            for buddy in log.buddies:
                if not self.findBuddyById(buddy.id):
                    self.buddies.append(buddy)

    def getUniqueDiveSpots(self):
        self.diveSpots = []
        for log in self.logs:
            if not self.findDiveSpotById(log.diveSpot.id):
                self.diveSpots.append(log.diveSpot)

    def getUniqueGasDefinitions(self):
        self.gasDefinitions = []
        for log in self.logs:
            if hasattr(log.diveGear, 'gasDefinition'):
                if hasattr(log.diveGear.gasDefinition, 'id'):
                    if not self.findGasDefinitionById(log.diveGear.gasDefinition.id):
                        self.gasDefinitions.append(log.diveGear.gasDefinition)

    def getUniqueMedia(self):
        self.media = []
        for log in self.logs:
            for medium in log.media:
                if not self.findMediumById(medium.id):
                    self.media.append(medium)

    def findDiveSpotById(self, diveSpotId):
        for diveSpot in self.diveSpots:
            if diveSpotId == diveSpot.id:
                return diveSpot

        return False

    def findGasDefinitionById(self, gasDefinitionId):
        for gasDefinition in self.gasDefinitions:
            if gasDefinitionId == gasDefinition.id:
                return gasDefinition

        return False

    def findMediumById(self, mediumId):
        for medium in self.media:
            if mediumId == medium.id:
                return medium

        return False

    def findEquipmentById(self, equipmentId):
        for item in self.equipment:
            if equipmentId == item.id:
                return item

        return False

    def findBuddyById(self, buddyId):
        for buddy in self.buddies:
            if buddyId == buddy.id:
                return buddy

        return False

###
# The big Log object with all its properties
#
class DeepbluLog:
    def __init__(self, jsonLog, media):
        self._start_epoch = None
        self.id = 'deepblu_dl_' + jsonLog.get('_id')
        self.diveDate = datetime.strptime(jsonLog.get('diveDTRaw'), "%Y,%m,%d,%H,%M,%S")
        self.airPressure = jsonLog.get('airPressure', 1000)
        self.waterType = jsonLog.get('waterType', 0)
        self.notes = escape(jsonLog.get('notes', ''))
        self.diveDuration = jsonLog.get('diveDuration', '')
        self.minTemp = DeepbluTools.convertTemp(jsonLog.get('diveMinTemperature', None))
        self.maxDepth = DeepbluTools.getDepth(jsonLog.get('diveMaxDepth', None), self.airPressure, self.waterType)
        self.diveGear = diveGear(jsonLog.get('_DiveGear', {}))
        # UDDF scheme prescribes for dive mode (i.e. apnea or scuba) to be included at waypoint level
        # as it is technically possible to change diving mode while diving
        # 'apnoe' is the German keyword used in UDDF < 3.2.2; using this for compatibility reasons
        self.diveMode = 'apnoe' if jsonLog.get('diveType') == 'Free' else 'opencircuit'
        self.diveProfile = diveProfile(jsonLog.get('_diveProfile'), self)
        self.diveSpot = diveSpot(jsonLog.get('divespot', {}))
        self.visibility = jsonLog.get('_DiveCondition', {}).get('visibility', None)
        self.airTemperature = jsonLog.get('_DiveCondition', {}).get('avgTemperature', None)
        if self.airTemperature:
            # for some obscure reason, this is not in decicelsius like elsewhere
            self.airTemperature = DeepbluTools.convertTemp(self.airTemperature*10)
        self.averageDepth = DeepbluTools.getDepth(jsonLog.get('_DiveCondition', {}).get('averageDepth', None), self.airPressure, self.waterType)
        
        self.buddies = []
        for buddy in jsonLog.get('diveBuddiesObj', {}):
            self.buddies.append(Diver(buddy))

        self.media = []
        for medium in media:
            self.media.append(Medium(medium))

###
# This is a diver (person). For now this is only buddies.
# Owner should probably extend or implement this class
# But since we're only setting properties and this is Python,
# it doesn't really matter?
# 
class Diver:
    def __init__(self, diver):
        self.id = diver.get('diveBuddyUserId')
        self.name = escape(diver.get('diveBuddyUserName'))

###
# Singular of media, i.c. videos and photos
# This program does not download your videos
# and photos (yet), but it does keep a reference
# 
class Medium:
    def __init__(self, medium):
        self.id = 'deepblu_md_' + medium.get('_id')
        self.url = medium.get('url')
        self.caption = escape(medium.get('caption', ''))
        timestamp = medium.get('timestamp')
        if timestamp:
            self.datetime = datetime.fromtimestamp(timestamp).isoformat()
        if medium.get('type') == "Video":
            self.type = 'video'
        else:
            self.type = 'image'

###
# All gear, including list of equipment
# Clumsy class, really. My bad
# 
class diveGear:
    def __init__(self, diveGear):
        self.gasDefinition = gasDefinition(diveGear.get('airMix'))
        self.tankVolume = diveGear.get('airTank', {}).get('volume')
        if diveGear.get('endBar'):
            self.endBar = int(diveGear.get('endBar')) * 10**5
        if diveGear.get('startedBar'):
            self.startBar = int(diveGear.get('startedBar')) * 10**5
        self.suit = diveGear.get('suitType')
        self.equipment = []
        for divecomputer in diveGear.get('diveComputer', {}):
            self.equipment.append(Equipment('divecomputer', divecomputer))

###
# Every piece of equipment is of a certain type, and has a manufacturer and model
# 
class Equipment:
    def __init__(self, kind, brandModel):
        self.type = kind
        self.brand = escape(str(brandModel.get('brand')))
        self.model = escape(str(brandModel.get('officialModel')))
        self.id = 'eq_' + hashlib.sha1((self.brand + self.model).encode('UTF-8')).hexdigest()[0:8]

###
# Deepblu only saves nitrogen and oxygen values for air mixes
# 
class gasDefinition:
    def __init__(self, airmix):
        if not airmix:
            return None

        self.o2 = airmix / 100
        self.n2 = (100 - airmix) / 100
        self.id = "mix" + str(airmix)
        self.name = str(airmix) + "/" + str(100 - airmix)

###
# diveProfile consists of wayPoints
# 'root' refers to dive log
# 
class diveProfile:
    def __init__(self, diveprofile, root):
        self.time = 0  # keeps track of time for waypoints
        self.waypoints = []
        for waypoint in diveprofile:
            self.waypoints.append(wayPoint(waypoint, root, self))

###
# wayPoint contains depth, temperature and time
# think of it as a dive computer sample point
# 'parent' refers to diveProfile; 'root' to DeepbluLog
# 
class wayPoint:
    def __init__(self, waypoint, root, parent):
        # convert from millibar to water depth
        airPressure = root.airPressure
        waterType = root.waterType
        depth = DeepbluTools.getDepth(waypoint.get('pressure'), airPressure, waterType)

        # A quirk of Deepblu is that, for some logs, it saves the dive time of waypoints
        # in Unix epoch time. This is why we keep track of the first waypoint time
        # and subtract it later from each following waypoint's time
        if root._start_epoch == None:
            root._start_epoch = waypoint.get('time') if waypoint.get('time') else 0
        # For some logs, Deepblu does not save time correctly, however Deepblu
        # always keeps a waypoint every 20 seconds. So if no time is set, add 20 s
        parent.time = waypoint.get('time') if waypoint.get('time') else parent.time + 20
        parent.time -= root._start_epoch  # subtract 0 or unix time from each waypoint
        
        self.depth = depth
        self.time = parent.time
        self.diveMode = root.diveMode # 'apnoe' for freediving; 'opencircuit' for scuba
        self.temp = DeepbluTools.convertTemp(waypoint.get('temperature')) # convert to Kelvin


class diveSpot:
    def __init__(self, divespot):
        self.id = 'deepblu_ds_' + str(divespot.get('_id'))
        self.name = escape(str(divespot.get('divespot')))
        self.lat = divespot.get('gpsLocation', {}).get('lat')
        self.lon = divespot.get('gpsLocation', {}).get('lng')
