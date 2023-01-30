import datetime
from distutils.log import Log

from deepblu_tools.models import deepblu as dm
from deepblu_tools.models import uddf as um


# Logbook (contains multiple logs, media, divespots,
# gas definitions, buddies, equipment)
class DeepbluLogBook:
    def __init__(self, posts: list, deepblu_user: "dm.DeepbluUser", max_posts: int):
        self.logs = []

        for post in posts:
            if (
                max_posts is not None and len(self.logs) >= max_posts
            ):  # max posts reached; stop appending
                break

            self.logs.append(dm.DeepbluLog(post.get("diveLog"), post.get("medias")))

        self.get_unique_media()
        self.get_unique_dive_bases()
        self.get_unique_dive_spots()
        self.get_unique_gas_definitions()
        self.get_unique_buddies()
        self.get_unique_equipment()
        self.owner = deepblu_user.to_person_type()
        if self.owner:
            self.owner.equipment = um.EquipmentType(
                divecomputer=[e.to_uddf() for e in self.equipment]
            )

    def __len__(self):
        return len(self.logs)

    # Below functions eliminate duplicates from the summaries
    def get_unique_equipment(self):
        self.equipment = []
        for log in self.logs:
            for item in log.dive_gear.equipment:
                if not self.find_attr_by_id("equipment", item.id):
                    self.equipment.append(item)

    def get_unique_buddies(self):
        self.buddies = []
        for log in self.logs:
            for buddy in log.buddies:
                if not self.find_attr_by_id("buddies", buddy.id):
                    self.buddies.append(buddy)

    def get_unique_dive_spots(self):
        self.dive_spots = []
        for log in self.logs:
            if not self.find_attr_by_id("dive_spots", log.dive_spot.id):
                self.dive_spots.append(log.dive_spot)

    def get_unique_dive_bases(self):
        self.dive_bases = []
        for log in self.logs:
            if not self.find_attr_by_id("dive_bases", log.dive_base.id):
                self.dive_bases.append(log.dive_base)

    def get_unique_gas_definitions(self):
        self.gas_definitions = []
        for log in self.logs:
            if hasattr(log.dive_gear, "gas_definition"):
                if hasattr(log.dive_gear.gas_definition, "id"):
                    if not self.find_attr_by_id(
                        "gas_definitions", log.dive_gear.gas_definition.id
                    ):
                        self.gas_definitions.append(log.dive_gear.gas_definition)

    def get_unique_media(self):
        self.media = []
        for log in self.logs:
            for medium in log.media:
                if not self.find_attr_by_id("media", medium.id):
                    self.media.append(medium)

    def find_attr_by_id(self, attribute: str, id: str) -> list:
        try:
            return [item for item in getattr(self, attribute) if item.id == id][0]
        except Exception:
            return []

    def to_uddf(self) -> um.Uddf:
        uddf = um.Uddf(version="3.2.2")
        uddf.generator = um.Generator(
            name="Deepblu Backup Tool",
            version="2.0.0",
            type=um.GeneratorType.CONVERTER,
            manufacturer=um.ManufacturerType(
                id="bluppfisk",
                name="Sander Van de Moortel",
                contact=um.ContactType(
                    email="sander.vandemoortel@gmail.com",
                    homepage=["https://github.com/bluppfisk/deepblu-tools"],
                ),
            ),
            datetime=datetime.datetime.now().isoformat(),
        )
        uddf.divesite = um.Divesite(
            site=[s.to_uddf() for s in self.dive_spots],
            divebase=[b.to_uddf() for b in self.dive_bases],
        )
        uddf.profiledata = um.Profiledata(
            repetitiongroup=um.RepetitiongroupType(
                id="rep", dive=[d.to_uddf() for d in self.logs]
            )
        )
        uddf.gasdefinitions = um.Gasdefinitions(
            mix=[g.to_uddf() for g in self.gas_definitions]
        )
        uddf.diver = um.Diver(
            owner=self.owner, buddy=[b.to_uddf() for b in self.buddies]
        )
        uddf.mediadata = um.Mediadata([m.to_uddf() for m in self.media])

        return uddf
