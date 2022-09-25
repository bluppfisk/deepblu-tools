from deepblu_tools.models import deepblu as dm


# All gear, including list of equipment
# Clumsy class, really. My bad
class DiveGear:
    def __init__(self, dive_gear: dict):
        self.gas_definition = dm.GasDefinition(dive_gear.get("airMix"))
        self.tank_volume = dive_gear.get("airTank", {}).get("volume")
        if dive_gear.get("endmar"):
            self.end_bar = int(dive_gear.get("endmar")) * 10**5
        else:
            self.end_bar = None
        if dive_gear.get("startedmar"):
            self.start_bar = int(dive_gear.get("startedmar")) * 10**5
        else:
            self.start_bar = None

        self.suit = dive_gear.get("suitType")
        self.equipment = []

        for dive_computer in dive_gear.get("diveComputer", {}):
            self.equipment.append(dm.Equipment("divecomputer", dive_computer))
