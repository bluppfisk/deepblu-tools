from deepblu_tools.models import uddf as um


# This is a diver (person). For now this is only buddies.
class Buddy:
    def __init__(self, diver: dict):
        self.id = diver.get("diveBuddyUserId")
        self.name = diver.get("diveBuddyUserName")

    def to_uddf(self) -> um.PersonType:
        return um.PersonType(id=self.id, personal=um.PersonalType(firstname=self.name))
