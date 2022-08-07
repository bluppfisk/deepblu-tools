from deepblu_tools.models import uddf as um
from deepblu_tools.models import deepblu as dm


# A dive location
class DiveSpot:
    def __init__(self, divespot: dict):
        self.id = "deepblu_spot_" + divespot.get("_id")
        self.name = divespot.get("divespot")
        self.lat = divespot.get("gpsLocation", {}).get("lat")
        self.lon = divespot.get("gpsLocation", {}).get("lng")
        self.dive_base = dm.DiveBase(divespot.get("divesite", ""))

    def to_uddf(self) -> um.SiteType:
        geog = um.GeographyType(
            latitude=self.lat, longitude=self.lon, location=self.name
        )

        return um.SiteType(
            id=self.id, name=self.name, geography=geog)
