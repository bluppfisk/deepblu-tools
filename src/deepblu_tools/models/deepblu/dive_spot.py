from deepblu_tools.models import uddf as um


# A dive location
class DiveSpot:
    def __init__(self, divespot: dict):
        self.id = divespot.get("_id")
        self.name = divespot.get("divespot")
        self.lat = divespot.get("gpsLocation", {}).get("lat")
        self.lon = divespot.get("gpsLocation", {}).get("lat")

    def to_uddf(self) -> um.SiteType:
        geog = um.GeographyType(
            latitude=self.lat, longitude=self.lon, location=self.name
        )

        return um.SiteType(id=self.id, name=self.name, geography=geog)
