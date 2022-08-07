from deepblu_tools.models import uddf as um


# A dive location
class DiveBase:
    def __init__(self, name: str):
        self.name = name
        self.id = self.name.lower().replace(" ", "_")

    def to_uddf(self) -> um.DivebaseType:
        return um.DivebaseType(id=self.id, name=self.name)
