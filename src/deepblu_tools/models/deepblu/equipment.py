from deepblu_tools.models import uddf as um
import hashlib


# Every piece of equipment is of a certain type, and has a manufacturer and model
# actually just for the dive computer for now
class Equipment:
    def __init__(self, kind: str, brand_model: dict):
        self.type = kind
        self.brand = brand_model.get("brand")
        self.model = brand_model.get("officialModel")
        try:
            self.id = (
                "eq_"
                + hashlib.sha1((self.brand + self.model).encode("UTF-8")).hexdigest()[0:8]
            )
        except TypeError:
            self.id = None

    def to_uddf(self):
        return um.EquipmentPieceType(
            id=self.id,
            name=self.type,
            manufacturer=um.ManufacturerType(id=self.brand, name=self.brand),
            model=self.model,
        )
