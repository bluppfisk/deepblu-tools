from deepblu_tools.models import deepblu as dm
from deepblu_tools.models import uddf as um


# The dive profile consists of wayPoints
# 'root' refers to dive log
class DiveProfile:
    def __init__(self, dive_profile, root: dm.DeepbluLog):
        self.time = 0  # keeps track of time for waypoints
        self.way_points = []
        for way_point in dive_profile:
            self.way_points.append(dm.WayPoint(way_point, root, self))

    def to_uddf(self) -> um.SamplesType:
        return um.SamplesType(waypoint=[wp.to_uddf() for wp in self.way_points])
