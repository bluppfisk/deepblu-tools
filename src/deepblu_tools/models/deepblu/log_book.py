from deepblu_tools.models import uddf as um
from deepblu_tools.models import deepblu as dm
import datetime


# Logbook (contains multiple logs, media, divespots, gas definitions, buddies, equipment)
class DeepbluLogBook:
    def __init__(self, posts: list, deepblu_user: 'dm.DeepbluUser', max_posts: int):
        self.logs = []

        for post in posts:
            if (
                max_posts is not None and len(self.logs) >= max_posts
            ):  # max posts reached; stop appending
                break

            self.logs.append(dm.DeepbluLog(post.get("diveLog"), post.get("medias")))

        self.get_unique_media()
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
                if not self.find_equipment_by_id(item.id):
                    self.equipment.append(item)

    def get_unique_buddies(self):
        self.buddies = []
        for log in self.logs:
            for buddy in log.buddies:
                if not self.find_buddy_by_id(buddy.id):
                    self.buddies.append(buddy)

    def get_unique_dive_spots(self):
        # @TODO: group by divebase ('divesite')
        self.dive_spots = []
        for log in self.logs:
            if not self.find_dive_spot_by_id(log.dive_spot.id):
                self.dive_spots.append(log.dive_spot)

    def get_unique_gas_definitions(self):
        self.gas_definitions = []
        for log in self.logs:
            if hasattr(log.dive_gear, "gas_definition"):
                if hasattr(log.dive_gear.gas_definition, "id"):
                    if not self.find_gas_definitions_by_id(
                        log.dive_gear.gas_definition.id
                    ):
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
        uddf.divesite = um.Divesite(site=[s.to_uddf() for s in self.dive_spots])
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