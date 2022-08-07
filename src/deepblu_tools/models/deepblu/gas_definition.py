from deepblu_tools.models import uddf as um


# Deepblu only saves nitrogen and oxygen values for air mixes
class GasDefinition:
    def __init__(self, airmix):
        if not airmix:
            return None

        self.o2 = airmix / 100
        self.n2 = (100 - airmix) / 100
        self.id = "mix" + str(airmix)
        self.name = str(airmix) + "/" + str(100 - airmix)

    def to_uddf(self):
        return um.MixType(id=self.id, name=self.name, o2=self.o2, n2=self.n2)
