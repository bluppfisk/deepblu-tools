from datetime import datetime, timezone

from deepblu_tools import utils
from deepblu_tools.models import deepblu as dm
from deepblu_tools.models import uddf as um


class DeepbluLog:
    def __init__(self, json_log: dict, media: dict):
        self._start_epoch = None
        self.id = "deepblu_divelog_" + json_log.get("_id")
        dive_date = json_log.get("diveDTRawUTC")
        self.dive_date = datetime.fromtimestamp(dive_date, tz=timezone.utc).isoformat()
        self.air_pressure = json_log.get("airPressure", 1000)
        self.water_type = json_log.get("waterType", 0)
        self.notes = json_log.get("notes")
        self.dive_duration = json_log.get("diveDuration")
        self.min_temp = utils.convert_temp(json_log.get("diveMinTemperature", None))
        self.max_depth = utils.get_depth(
            json_log.get("diveMaxDepth", None), self.air_pressure, self.water_type
        )
        self.dive_gear = dm.DiveGear(json_log.get("_DiveGear", {}))
        # UDDF scheme prescribes for dive mode (i.e. apnea or scuba) to be
        # included at waypoint level as it is technically possible to change
        # diving mode while diving
        # 'apnoe' is the German keyword used in UDDF < 3.2.2;
        # using this for compatibility reasons
        self.dive_mode = (
            "apnoe" if json_log.get("diveType") == "Free" else "opencircuit"
        )
        self.dive_profile = dm.DiveProfile(json_log.get("_diveProfile"), self)
        self.dive_spot = dm.DiveSpot(json_log.get("divespot", {}))
        self.dive_base = self.dive_spot.dive_base
        self.visibility = json_log.get("_DiveCondition", {}).get("visibility", None)
        self.air_temperature = json_log.get("_DiveCondition", {}).get(
            "avgTemperature", None
        )
        if self.air_temperature:
            # For some obscure reason, this is not in decicelsius like elsewhere
            self.air_temperature = utils.convert_temp(self.air_temperature * 10)
        self.average_depth = utils.get_depth(
            json_log.get("_DiveCondition", {}).get("averageDepth", None),
            self.air_pressure,
            self.water_type,
        )

        self.buddies = []
        for buddy in json_log.get("diveBuddiesObj", {}):
            self.buddies.append(dm.Buddy(buddy))

        self.media = []
        for medium in media:
            self.media.append(dm.Medium(medium))

    def to_uddf(self) -> um.DiveType:
        return um.DiveType(
            id=self.id,
            informationafterdive=um.InformationafterdiveType(
                averagedepth=self.average_depth,
                diveduration=self.dive_duration,
                greatestdepth=self.max_depth,
                lowesttemperature=self.min_temp,
                notes=um.NotesType(
                    para=self.notes, link=[um.LinkType(ref=m.id) for m in self.media]
                ),
                visibility=self.visibility,
            ),
            tankdata=[
                um.TankdataType(
                    tankpressurebegin=self.dive_gear.start_bar,
                    tankpressureend=self.dive_gear.end_bar,
                    tankvolume=self.dive_gear.tank_volume,
                )
            ],
            samples=self.dive_profile.to_uddf(),
            informationbeforedive=um.InformationbeforediveType(
                airtemperature=self.air_temperature,
                datetime=self.dive_date,
                link=[um.LinkType(link.id) for link in self.buddies + [self.dive_spot]],
            ),
        )
