from deepblu_tools import utils
from deepblu_tools.models import uddf as um


# wayPoint contains depth, temperature and time
# think of it as a dive computer sample point
# 'parent' refers to diveProfile; 'root' to DeepbluLog
class WayPoint:
    def __init__(self, way_point, root, parent):
        # convert from millibar to water depth
        air_pressure = root.air_pressure
        water_type = root.water_type
        depth = utils.get_depth(way_point.get("pressure"), air_pressure, water_type)

        # A quirk of Deepblu is that, for some logs, it saves the dive time of waypoints
        # in Unix epoch time. This is why we keep track of the first waypoint time
        # and subtract it later from each following waypoint's time
        if root._start_epoch is None:
            root._start_epoch = way_point.get("time") if way_point.get("time") else 0
        # For some logs, Deepblu does not save time correctly, however Deepblu
        # always keeps a waypoint every 20 seconds. So if no time is set, add 20 s
        parent.time = (
            way_point.get("time") if way_point.get("time") else parent.time + 20
        )
        parent.time -= root._start_epoch  # subtract 0 or unix time from each waypoint

        self.depth = depth
        self.time = parent.time
        self.dive_mode = (
            root.dive_mode
        )  # 'apnoe' for freediving; 'opencircuit' for scuba
        self.temp = utils.convert_temp(
            way_point.get("temperature")
        )  # convert to Kelvin

    def to_uddf(self):
        return um.WaypointType(
            depth=self.depth,
            divetime=self.time,
            temperature=self.temp,
            divemode=um.WaypointType.Divemode(
                type=getattr(um.DivemodeType, self.dive_mode.upper())
            ),
        )
