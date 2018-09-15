# Logic and dataclasses to parse and contain logs as well as summaries
# for persons, equipment, gas definitions, media and divespots
# that may be referenced in the individual logs

import hashlib
from datetime import datetime
from xml.sax.saxutils import escape

from deepblu_tools import DeepbluTools

# Logbook (contains multiple logs, media, divespots, gas definitions, buddies, equipment)
class DeepbluLogBook:
    def __init__(self, posts, deepblu_user, max_posts):
        print ("Parse all the things!")
        self.logs = []
        self.owner = deepblu_user


        for post in posts:
            if max_posts is not None and len(self.logs) >= max_posts:  # max posts reached; stop appending
                break

            self.logs.append(DeepbluLog(post.get('diveLog'), post.get('medias')))

        self.get_unique_media()
        self.get_unique_dive_spots()
        self.get_unique_gas_definitions()
        self.get_unique_buddies()
        self.get_unique_equipment()

    def __len__(self):
        return len(self.logs)

    # Below functions eliminate duplicates from the summaries
    def get_unique_equipment(self):
        self.equipment = []
        for log in self.logs:
            for item in log.dive_gear.equipment:
                if not self.find_equipment_by_id(item.id):
                    self.equipment.append(item)

    def get_unique_buddies(self):
        self.buddies = []
        for log in self.logs:
            for buddy in log.buddies:
                if not self.find_buddy_by_id(buddy.id):
                    self.buddies.append(buddy)

    def get_unique_dive_spots(self):
        self.dive_spots = []
        for log in self.logs:
            if not self.find_dive_spot_by_id(log.dive_spot.id):
                self.dive_spots.append(log.dive_spot)

    def get_unique_gas_definitions(self):
        self.gas_definitions = []
        for log in self.logs:
            if hasattr(log.dive_gear, 'gasDefinition'):
                if hasattr(log.dive_gear.gas_definition, 'id'):
                    if not self.find_gas_definitions_by_id(log.dive_gear.gas_definition.id):
                        self.gas_definitions.append(log.dive_gear.gas_definition)

    def get_unique_media(self):
        self.media = []
        for log in self.logs:
            for medium in log.media:
                if not self.find_medium_by_id(medium.id):
                    self.media.append(medium)

    def find_dive_spot_by_id(self, dive_spot_id):
        for dive_spot in self.dive_spots:
            if dive_spot_id == dive_spot.id:
                return dive_spot

        return False

    def find_gas_definitions_by_id(self, gas_definition_id):
        for gas_definition in self.gas_definitions:
            if gas_definition_id == gas_definition.id:
                return gas_definition

        return False

    def find_medium_by_id(self, medium_id):
        for medium in self.media:
            if medium_id == medium.id:
                return medium

        return False

    def find_equipment_by_id(self, equipment_id):
        for item in self.equipment:
            if equipment_id == item.id:
                return item

        return False

    def find_buddy_by_id(self, buddyId):
        for buddy in self.buddies:
            if buddyId == buddy.id:
                return buddy

        return False


# A Deepblu dive log with its properties
class DeepbluLog:
    def __init__(self, json_log, media):
        self._start_epoch = None
        self.id = 'deepblu_dl_' + json_log.get('_id')
        self.dive_date = datetime.strptime(json_log.get('diveDTRaw'), "%Y,%m,%d,%H,%M,%S")
        self.air_pressure = json_log.get('airPressure', 1000)
        self.water_type = json_log.get('waterType', 0)
        self.notes = escape(json_log.get('notes', ''))
        self.dive_duration = json_log.get('diveDuration', '')
        self.min_temp = DeepbluTools.convert_temp(json_log.get('diveMinTemperature', None))
        self.max_depth = DeepbluTools.get_depth(json_log.get('diveMaxDepth', None), self.air_pressure, self.water_type)
        self.dive_gear = DiveGear(json_log.get('_DiveGear', {}))
        # UDDF scheme prescribes for dive mode (i.e. apnea or scuba) to be included at waypoint level
        # as it is technically possible to change diving mode while diving
        # 'apnoe' is the German keyword used in UDDF < 3.2.2; using this for compatibility reasons
        self.dive_mode = 'apnoe' if json_log.get('diveType') == 'Free' else 'opencircuit'
        self.dive_profile = DiveProfile(json_log.get('_diveProfile'), self)
        self.dive_spot = DiveSpot(json_log.get('divespot', {}))
        self.visibility = json_log.get('_DiveCondition', {}).get('visibility', None)
        self.air_temperature = json_log.get('_DiveCondition', {}).get('avgTemperature', None)
        if self.air_temperature:
            # For some obscure reason, this is not in decicelsius like elsewhere
            self.air_temperature = DeepbluTools.convert_temp(self.air_temperature*10)
        self.average_depth = DeepbluTools.get_depth(json_log.get('_DiveCondition', {}).get('averageDepth', None), self.air_pressure, self.water_type)
        
        self.buddies = []
        for buddy in json_log.get('diveBuddiesObj', {}):
            self.buddies.append(Diver(buddy))

        self.media = []
        for medium in media:
            self.media.append(Medium(medium))


# This is a diver (person). For now this is only buddies.
class Diver:
    def __init__(self, diver):
        self.id = diver.get('diveBuddyUserId')
        self.name = escape(diver.get('diveBuddyUserName'))


# Singular of media, i.c. videos and photos
# This program does not download your videos
# and photos (yet), but it does keep a reference
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


# All gear, including list of equipment
# Clumsy class, really. My bad
class DiveGear:
    def __init__(self, dive_gear):
        self.gas_definition = GasDefinition(dive_gear.get('airMix'))
        self.tank_volume = dive_gear.get('airTank', {}).get('volume')
        if dive_gear.get('endBar'):
            self.end_bar = int(dive_gear.get('endBar')) * 10**5
        if dive_gear.get('startedBar'):
            self.start_bar = int(dive_gear.get('startedBar')) * 10**5
        self.suit = dive_gear.get('suitType')
        self.equipment = []
        for dive_computer in dive_gear.get('diveComputer', {}):
            self.equipment.append(Equipment('divecomputer', dive_computer))


# Every piece of equipment is of a certain type, and has a manufacturer and model
class Equipment:
    def __init__(self, kind, brand_model):
        self.type = kind
        self.brand = escape(str(brand_model.get('brand')))
        self.model = escape(str(brand_model.get('officialModel')))
        self.id = 'eq_' + hashlib.sha1((self.brand + self.model).encode('UTF-8')).hexdigest()[0:8]


# Deepblu only saves nitrogen and oxygen values for air mixes
class GasDefinition:
    def __init__(self, airmix):
        if not airmix:
            return None

        self.o2 = airmix / 100
        self.n2 = (100 - airmix) / 100
        self.id = "mix" + str(airmix)
        self.name = str(airmix) + "/" + str(100 - airmix)


# The dive profile consists of wayPoints
# 'root' refers to dive log
class DiveProfile:
    def __init__(self, dive_profile, root):
        self.time = 0  # keeps track of time for waypoints
        self.way_points = []
        for way_point in dive_profile:
            self.way_points.append(WayPoint(way_point, root, self))


# wayPoint contains depth, temperature and time
# think of it as a dive computer sample point
# 'parent' refers to diveProfile; 'root' to DeepbluLog
class WayPoint:
    def __init__(self, way_point, root, parent):
        # convert from millibar to water depth
        air_pressure = root.air_pressure
        water_type = root.water_type
        depth = DeepbluTools.get_depth(way_point.get('pressure'), air_pressure, water_type)

        # A quirk of Deepblu is that, for some logs, it saves the dive time of waypoints
        # in Unix epoch time. This is why we keep track of the first waypoint time
        # and subtract it later from each following waypoint's time
        if root._start_epoch == None:
            root._start_epoch = way_point.get('time') if way_point.get('time') else 0
        # For some logs, Deepblu does not save time correctly, however Deepblu
        # always keeps a waypoint every 20 seconds. So if no time is set, add 20 s
        parent.time = way_point.get('time') if way_point.get('time') else parent.time + 20
        parent.time -= root._start_epoch  # subtract 0 or unix time from each waypoint
        
        self.depth = depth
        self.time = parent.time
        self.dive_mode = root.dive_mode # 'apnoe' for freediving; 'opencircuit' for scuba
        self.temp = DeepbluTools.convert_temp(way_point.get('temperature')) # convert to Kelvin

# A dive location
class DiveSpot:
    def __init__(self, dive_spot):
        self.id = 'deepblu_ds_' + str(dive_spot.get('_id'))
        self.name = escape(str(dive_spot.get('divespot')))
        self.lat = dive_spot.get('gpsLocation', {}).get('lat')
        self.lon = dive_spot.get('gpsLocation', {}).get('lng')
