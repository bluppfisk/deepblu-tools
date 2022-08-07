from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.streit.cc/uddf/3.2/"


@dataclass
class IdType:
    class Meta:
        name = "ID_TYPE"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class AbundanceOccurence(Enum):
    NOT_ASCERTAINABLE = "not-ascertainable"
    SINGLE_INDIVIDUAL = "single-individual"
    LOOSE_ASSOCIATION = "loose-association"
    SWARM = "swarm"
    COLONY = "colony"


class AbundanceQuality(Enum):
    EXACT = "exact"
    ESTIMATED = "estimated"


@dataclass
class AddressType:
    class Meta:
        name = "addressType"

    street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    postcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    province: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


class AlarmType(Enum):
    ASCENT = "ascent"
    BREATH = "breath"
    DECO = "deco"
    ERROR = "error"
    LINK = "link"
    MICROBUBBLES = "microbubbles"
    RBT = "rbt"
    SKINCOOLING = "skincooling"
    SURFACE = "surface"


@dataclass
class ApplicationdataType:
    class Meta:
        name = "applicationdataType"

    decotrainer: Optional["ApplicationdataType.Decotrainer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    hargikas: Optional["ApplicationdataType.Hargikas"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    heinrichsweikamp: Optional["ApplicationdataType.Heinrichsweikamp"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tausim: Optional["ApplicationdataType.Tausim"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tautabu: Optional["ApplicationdataType.Tautabu"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )

    @dataclass
    class Decotrainer:
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )

    @dataclass
    class Hargikas:
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )

    @dataclass
    class Heinrichsweikamp:
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )

    @dataclass
    class Tausim:
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )

    @dataclass
    class Tautabu:
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )


@dataclass
class BottomtimetablescopeType:
    class Meta:
        name = "bottomtimetablescopeType"

    divedepthbegin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    divedepthend: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    divedepthstep: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    breathingconsumptionvolumebegin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    breathingconsumptionvolumeend: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    breathingconsumptionvolumestep: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    tankvolumebegin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    tankvolumeend: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    tankvolumestep: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    tankpressurebegin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    tankpressurereserve: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class ContactType:
    class Meta:
        name = "contactType"

    language: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    phone: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    mobilephone: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    fax: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    homepage: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class DcalarmType:
    class Meta:
        name = "dcalarmType"

    acknowledge: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    alarm_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "alarmType",
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class DcalarmtimeType:
    class Meta:
        name = "dcalarmtimeType"

    acknowledge: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    alarm_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "alarmType",
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class DcbuddydataType:
    class Meta:
        name = "dcbuddydataType"

    buddy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DcdivesitedataType:
    class Meta:
        name = "dcdivesitedataType"

    divesite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DcgasdefinitionsdataType:
    class Meta:
        name = "dcgasdefinitionsdataType"

    setdcallgasdefinitions: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    setdcgasdata: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


class DecostopKind(Enum):
    SAFETY = "safety"
    MANDATORY = "mandatory"


@dataclass
class DimensionType:
    class Meta:
        name = "dimensionType"

    length: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    beam: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    draught: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    displacement: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tonnage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


class DivemodeType(Enum):
    APNEA = "apnea"
    APNOE = "apnoe"
    CLOSEDCIRCUIT = "closedcircuit"
    OPENCIRCUIT = "opencircuit"
    SEMICLOSEDCIRCUIT = "semiclosedcircuit"


class DrugTypePeriodicallytaken(Enum):
    NO = "no"
    YES = "yes"


@dataclass
class EncapsulatedDateTimeType:
    class Meta:
        name = "encapsulatedDateTimeType"

    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


class ExaminationTypeExaminationresult(Enum):
    PASSED = "passed"
    FAILED = "failed"


class ExposuretoaltitudeTypeTransportation(Enum):
    COMMERCIAL_AIRCRAFT = "commercial-aircraft"
    UNPRESSURIZED_AIRCRAFT = "unpressurized-aircraft"
    MEDEVAC_AIRCRAFT = "medevac-aircraft"
    GROUND_TRANSPORTATION = "ground-transportation"
    HELICOPTER = "helicopter"


class GeneratorType(Enum):
    CONVERTER = "converter"
    DIVECOMPUTER = "divecomputer"
    LOGBOOK = "logbook"


@dataclass
class GetdcdataType:
    class Meta:
        name = "getdcdataType"

    getdcalldata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    getdcgeneratordata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    getdcownerdata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    getdcbuddydata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    getdcgasdefinitionsdata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    getdcdivesitedata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    getdcdivetripdata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    getdcprofiledata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )


class GlobalalarmsgivenGlobalalarm(Enum):
    ASCENT_WARNING_TOO_LONG = "ascent-warning-too-long"
    SOS_MODE = "sos-mode"
    WORK_TOO_HARD = "work-too-hard"


class GloballightintensityType(Enum):
    UNDETERMINED = "undetermined"
    SUNNY = "sunny"
    HALF_SHADOW = "half-shadow"
    SHADOW = "shadow"
    NO_LIGHT = "no-light"


class ImagedataMeteringmethod(Enum):
    SPOT = "spot"
    CENTERWEIGHTED = "centerweighted"
    MATRIX = "matrix"


class InformationafterdiveTypeCurrent(Enum):
    NO_CURRENT = "no-current"
    VERY_MILD_CURRENT = "very-mild-current"
    MILD_CURRENT = "mild-current"
    MODERATE_CURRENT = "moderate-current"
    HARD_CURRENT = "hard-current"
    VERY_HARD_CURRENT = "very-hard-current"


class InformationafterdiveTypeDiveplan(Enum):
    NONE = "none"
    TABLE = "table"
    DIVE_COMPUTER = "dive-computer"
    ANOTHER_DIVER = "another-diver"


class InformationafterdiveTypeDivetable(Enum):
    PADI = "PADI"
    NAUI = "NAUI"
    BSAC = "BSAC"
    BUEHLMANN = "Buehlmann"
    DCIEM = "DCIEM"
    US_NAVY = "US-Navy"
    CSMD = "CSMD"
    COMEX = "COMEX"
    OTHER = "other"


class InformationafterdiveTypeEquipmentmalfunction(Enum):
    NONE = "none"
    FACE_MASK = "face-mask"
    FINS = "fins"
    WEIGHT_BELT = "weight-belt"
    BUOYANCY_CONTROL_DEVICE = "buoyancy-control-device"
    THERMAL_PROTECTION = "thermal-protection"
    DIVE_COMPUTER = "dive-computer"
    DEPTH_GAUGE = "depth-gauge"
    PRESSURE_GAUGE = "pressure-gauge"
    BREATHING_APPARATUS = "breathing-apparatus"
    DECO_REEL = "deco-reel"
    OTHER = "other"


class InformationafterdiveTypeProblems(Enum):
    NONE = "none"
    EQUALISATION = "equalisation"
    VERTIGO = "vertigo"
    OUT_OF_AIR = "out-of-air"
    BUOYANCY = "buoyancy"
    SHARED_AIR = "shared-air"
    RAPID_ASCENT = "rapid-ascent"
    SEA_SICKNESS = "sea-sickness"
    OTHER = "other"


class InformationafterdiveTypeProgram(Enum):
    RECREATION = "recreation"
    TRAINING = "training"
    SCIENTIFIC = "scientific"
    MEDICAL = "medical"
    COMMERCIAL = "commercial"
    MILITARY = "military"
    COMPETITIVE = "competitive"
    OTHER = "other"


class InformationafterdiveTypeThermalcomfort(Enum):
    NOT_INDICATED = "not-indicated"
    COMFORTABLE = "comfortable"
    COLD = "cold"
    VERY_COLD = "very-cold"
    HOT = "hot"


class InformationafterdiveTypeWorkload(Enum):
    NOT_SPECIFIED = "not-specified"
    RESTING = "resting"
    LIGHT = "light"
    MODERATE = "moderate"
    SEVERE = "severe"
    EXHAUSTING = "exhausting"


class InformationbeforediveTypeApparatus(Enum):
    OPEN_SCUBA = "open-scuba"
    REBREATHER = "rebreather"
    SURFACE_SUPPLIED = "surface-supplied"
    CHAMBER = "chamber"
    EXPERIMENTAL = "experimental"


class InformationbeforediveTypePlatform(Enum):
    BEACH_SHORE = "beach-shore"
    PIER = "pier"
    SMALL_BOAT = "small-boat"
    CHARTER_BOAT = "charter-boat"
    LIVE_ABOARD = "live-aboard"
    BARGE = "barge"
    LANDSIDE = "landside"
    HYPERBARIC_FACILITY = "hyperbaric-facility"
    OTHER = "other"


class InformationbeforediveTypePurpose(Enum):
    SIGHTSEEING = "sightseeing"
    LEARNING = "learning"
    TEACHING = "teaching"
    RESEARCH = "research"
    PHOTOGRAPHY_VIDEOGRAPHY = "photography-videography"
    SPEARFISHING = "spearfishing"
    PROFICIENCY = "proficiency"
    WORK = "work"
    OTHER = "other"


class InformationbeforediveTypeStateofrestbeforedive(Enum):
    NOT_SPECIFIED = "not-specified"
    RESTED = "rested"
    TIRED = "tired"
    EXHAUSTED = "exhausted"


@dataclass
class LinkType:
    class Meta:
        name = "linkType"

    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OutputType:
    class Meta:
        name = "outputType"

    lingo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    fileformat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    headline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


class PersonalTypeSmoking(Enum):
    VALUE_0 = "0"
    VALUE_0_3 = "0-3"
    VALUE_4_10 = "4-10"
    VALUE_11_20 = "11-20"
    VALUE_21_40 = "21-40"
    VALUE_40 = "40+"


@dataclass
class PriceType:
    class Meta:
        name = "priceType"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "length": 3,
        }
    )


@dataclass
class RatingType:
    class Meta:
        name = "ratingType"

    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    ratingvalue: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 10,
        }
    )


class Setpo2Setby(Enum):
    USER = "user"
    COMPUTER = "computer"


class SexType(Enum):
    UNDETERMINED = "undetermined"
    MALE = "male"
    FEMALE = "female"
    HERMAPHRODITE = "hermaphrodite"


@dataclass
class SimpleNamedType:
    class Meta:
        name = "simpleNamedType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    aliasname: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


class SiteTypeEnvironment(Enum):
    UNKNOWN = "unknown "
    OCEAN_SEA = "ocean-sea"
    LAKE_QUARRY = "lake-quarry"
    RIVER_SPRING = "river-spring"
    CAVE_CAVERN = "cave-cavern"
    POOL = "pool"
    HYPERBARIC_CHAMBER = "hyperbaric-chamber"
    UNDER_ICE = "under-ice"
    OTHER = "other"


class SpeciesTypeDominance(Enum):
    UNDETERMINED = "undetermined"
    LESS_THAN_1_20 = "less-than-1/20"
    VALUE_1_20_UP_TO_1_4 = "1/20-up-to-1/4"
    VALUE_1_4_UP_TO_1_2 = "1/4-up-to-1/2"
    VALUE_1_2_UP_TO_3_4 = "1/2-up-to-3/4"
    GREATER_THAN_3_4 = "greater-than-3/4"
    SINGLE_INDIVIDUAL = "single-individual"


class SpeciesTypeLifestage(Enum):
    LARVA = "larva"
    JUVENILE = "juvenile"
    ADULT = "adult"


class SuitTypeSuittype(Enum):
    DIVE_SKIN = "dive-skin"
    WET_SUIT = "wet-suit"
    DRY_SUIT = "dry-suit"
    HOT_WATER_SUIT = "hot-water-suit"
    OTHER = "other"


@dataclass
class TablescopeType:
    class Meta:
        name = "tablescopeType"

    altitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divedepthbegin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divedepthend: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divedepthstep: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bottomtimemaximum: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bottomtimeminimum: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bottomtimestepbegin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bottomtimestepend: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


class TankmaterialType(Enum):
    ALUMINIUM = "aluminium"
    CARBON = "carbon"
    STEEL = "steel"


class TissueTypeGas(Enum):
    H2 = "h2"
    HE = "he"
    N2 = "n2"


@dataclass
class WayaltitudeType:
    class Meta:
        name = "wayaltitudeType"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    waytime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BottomtimetableType(IdType):
    class Meta:
        name = "bottomtimetableType"

    title: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    output: Optional[OutputType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    applicationdata: Optional[ApplicationdataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bottomtimetablescope: Optional[BottomtimetablescopeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class BuiltType:
    class Meta:
        name = "builtType"

    shipyard: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    launchingdate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class DcalarmWithDepthType:
    class Meta:
        name = "dcalarmWithDepthType"

    dcalarmdepth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    dcalarm: Optional[DcalarmType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class DcalarmWithTimeType(EncapsulatedDateTimeType):
    class Meta:
        name = "dcalarmWithTimeType"

    dcalarm: Optional[DcalarmType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class DcdecomodelType(SimpleNamedType):
    class Meta:
        name = "dcdecomodelType"

    applicationdata: Optional[ApplicationdataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class DcdivedepthalarmType:
    class Meta:
        name = "dcdivedepthalarmType"

    dcalarmdepth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    dcalarm: Optional[DcalarmType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class Dcdivepo2AlarmType:
    class Meta:
        name = "dcdivepo2alarmType"

    maximumpo2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    dcalarm: Optional[DcalarmType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class DcdivetimealarmType:
    class Meta:
        name = "dcdivetimealarmType"

    timespan: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    dcalarm: Optional[DcalarmType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class DcendndtalarmType:
    class Meta:
        name = "dcendndtalarmType"

    dcalarm: Optional[DcalarmType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class DivecomputerdumpType:
    class Meta:
        name = "divecomputerdumpType"

    link: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    dcdump: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class ExposuretoaltitudeType:
    class Meta:
        name = "exposuretoaltitudeType"

    surfaceintervalbeforealtitudeexposure: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    transportation: Optional[ExposuretoaltitudeTypeTransportation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    dateofflight: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    altitudeofexposure: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    totallengthofexposure: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class GeographyType:
    class Meta:
        name = "geographyType"

    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    altitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    timezone: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class GuideType(IdType):
    class Meta:
        name = "guideType"

    link: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class LightintensityType:
    class Meta:
        name = "lightintensityType"

    value: Optional[GloballightintensityType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    lux: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaType(IdType):
    class Meta:
        name = "mediaType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    objectname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class NamedType(IdType):
    class Meta:
        name = "namedType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    aliasname: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class NotesType:
    class Meta:
        name = "notesType"

    para: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class PersonalType:
    class Meta:
        name = "personalType"

    firstname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    middlename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lastname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    birthname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    honorific: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    sex: Optional[SexType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    birthdate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    passport: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    membership: Optional["PersonalType.Membership"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    weight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bloodgroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    smoking: Optional[PersonalTypeSmoking] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    numberofdives: Optional["PersonalType.Numberofdives"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )

    @dataclass
    class Membership:
        organisation: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        memberid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Numberofdives:
        startdate: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        enddate: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        dives: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class PriceperdivepackageType(PriceType):
    class Meta:
        name = "priceperdivepackageType"

    noofdives: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TankdataType:
    class Meta:
        name = "tankdataType"

    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tankvolume: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tankpressurebegin: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    tankpressureend: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    breathingconsumptionvolume: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class TissueType:
    class Meta:
        name = "tissueType"

    gas: Optional[TissueTypeGas] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    halflife: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class WaypointType:
    class Meta:
        name = "waypointType"

    alarm: List["WaypointType.Alarm"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    batterychargecondition: List["WaypointType.Batterychargecondition"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    cns: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    decostop: List["WaypointType.Decostop"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bodytemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    calculatedpo2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    depth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divetime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    heading: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    otu: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    pulserate: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    remainingbottomtime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    remainingo2time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setmarker: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setpo2: Optional["WaypointType.Setpo2"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    switchmix: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tankpressure: List["WaypointType.Tankpressure"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    temperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divemode: Optional["WaypointType.Divemode"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    gradientfactor: Optional["WaypointType.Gradientfactor"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    measuredpo2: List["WaypointType.Measuredpo2"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    nodecotime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )

    @dataclass
    class Alarm:
        value: Optional[AlarmType] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        level: Optional[float] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Batterychargecondition:
        value: Optional[float] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        deviceref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        tankref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Decostop:
        kind: Optional[DecostopKind] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        decodepth: Optional[float] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        duration: Optional[float] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Setpo2:
        value: Optional[float] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        setby: Optional[Setpo2Setby] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Tankpressure:
        value: Optional[float] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Divemode:
        type: Optional[DivemodeType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Gradientfactor:
        value: Optional[float] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        tissue: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Measuredpo2:
        value: Optional[float] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        ref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class AccommodationType(NamedType):
    class Meta:
        name = "accommodationType"

    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    rating: List[RatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class BuehlmannType(IdType):
    class Meta:
        name = "buehlmannType"

    tissue: List[TissueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_occurs": 1,
        }
    )
    gradientfactorhigh: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    gradientfactorlow: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class CaveType(NamedType):
    class Meta:
        name = "caveType"

    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class DivebaseType(NamedType):
    class Meta:
        name = "divebaseType"

    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    priceperdive: Optional[PriceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    pricedivepackage: Optional[PriceperdivepackageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    guide: List[GuideType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    rating: List[RatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    link: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class DrugType(SimpleNamedType):
    class Meta:
        name = "drugType"

    periodicallytaken: Optional[DrugTypePeriodicallytaken] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    timespanbeforedive: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class EquipmentconfigurationType(NamedType):
    class Meta:
        name = "equipmentconfigurationType"

    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_occurs": 1,
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class ImageType(MediaType):
    class Meta:
        name = "imageType"

    imagedata: Optional["ImageType.Imagedata"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Imagedata:
        aperture: Optional[float] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )
        datetime: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )
        exposurecompensation: Optional[float] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )
        filmspeed: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )
        focallength: Optional[float] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )
        focusingdistance: Optional[float] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )
        meteringmethod: Optional[ImagedataMeteringmethod] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )
        shutterspeed: Optional[float] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )


@dataclass
class IndividualType(IdType):
    class Meta:
        name = "individualType"

    personal: Optional[PersonalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class IndoorType(SimpleNamedType):
    class Meta:
        name = "indoorType"

    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class InputprofileType:
    class Meta:
        name = "inputprofileType"

    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    waypoint: List[WaypointType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_occurs": 1,
        }
    )


@dataclass
class InsuranceType:
    class Meta:
        name = "insuranceType"

    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    aliasname: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    issuedate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    validdate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class ManufacturerType(NamedType):
    class Meta:
        name = "manufacturerType"

    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class MixType(NamedType):
    class Meta:
        name = "mixType"

    o2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    n2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    he: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    ar: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    h2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    priceperlitre: Optional[PriceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    maximumpo2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    maximumoperationdepth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    equivalentairdepth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class MixchangeType:
    class Meta:
        name = "mixchangeType"

    ascent: Optional["MixchangeType.Ascent"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    descent: Optional["MixchangeType.Descent"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )

    @dataclass
    class Ascent:
        waypoint: List[WaypointType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Descent:
        waypoint: List[WaypointType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )


@dataclass
class OperatorType(SimpleNamedType):
    class Meta:
        name = "operatorType"

    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    rating: List[RatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class PermitType:
    class Meta:
        name = "permitType"

    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    aliasname: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    issuedate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    validdate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class PlaceType(SimpleNamedType):
    class Meta:
        name = "placeType"

    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class RgbmType(IdType):
    class Meta:
        name = "rgbmType"

    tissue: List[TissueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_occurs": 1,
        }
    )


@dataclass
class SamplesType:
    class Meta:
        name = "samplesType"

    waypoint: List[WaypointType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_occurs": 1,
        }
    )


@dataclass
class SetdcdataType:
    class Meta:
        name = "setdcdataType"

    setdcalarmtime: List[DcalarmWithTimeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcaltitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcbuddydata: Optional[DcbuddydataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcdatetime: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcdecomodel: Optional[DcdecomodelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcdivedepthalarm: List[DcalarmWithDepthType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcdivepo2alarm: List[Dcdivepo2AlarmType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcdivesitedata: Optional[DcdivesitedataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcdivetimealarm: List[DcdivetimealarmType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcendndtalarm: Optional[DcendndtalarmType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcgasdefinitionsdata: Optional[DcgasdefinitionsdataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcownerdata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    setdcpassword: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    setdcgeneratordata: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )


@dataclass
class ShopType(NamedType):
    class Meta:
        name = "shopType"

    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class SpeciesType(IdType):
    class Meta:
        name = "speciesType"

    trivialname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    scientificname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    abundance: Optional["SpeciesType.Abundance"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    sex: Optional[SexType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lifestage: Optional[SpeciesTypeLifestage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lightintensity: Optional[LightintensityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    dominance: Optional[SpeciesTypeDominance] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    size: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )

    @dataclass
    class Abundance:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        quality: Optional[AbundanceQuality] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        occurence: Optional[AbundanceOccurence] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class SurfaceintervalType:
    class Meta:
        name = "surfaceintervalType"

    infinity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    passedtime: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    wayaltitude: List[WayaltitudeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    exposuretoaltitude: Optional[ExposuretoaltitudeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class VesselType(NamedType):
    class Meta:
        name = "vesselType"

    shiptype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    marina: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    contact: Optional[ContactType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    shipdimension: Optional[DimensionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    rating: List[RatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class VpmType(IdType):
    class Meta:
        name = "vpmType"

    gamma: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    gc: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lambda_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    r0: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tissue: List[TissueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_occurs": 1,
        }
    )


@dataclass
class WreckType(SimpleNamedType):
    class Meta:
        name = "wreckType"

    shiptype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    nationality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    built: Optional[BuiltType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    shipdimension: Optional[DimensionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    sunk: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class BaseCalculationType(IdType):
    class Meta:
        name = "baseCalculationType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    surfaceintervalafterdive: Optional[SurfaceintervalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    surfaceintervalbeforedive: Optional[SurfaceintervalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    density: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    maximumascendingrate: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    output: Optional[OutputType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    applicationdata: Optional[ApplicationdataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    decomodel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    deepstoptime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    mixchange: Optional[MixchangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    inputprofile: Optional[InputprofileType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class Business:
    class Meta:
        name = "business"
        namespace = "http://www.streit.cc/uddf/3.2/"

    shop: List[ShopType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Divecomputercontrol:
    class Meta:
        name = "divecomputercontrol"
        namespace = "http://www.streit.cc/uddf/3.2/"

    setdcdata: Optional[SetdcdataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    getdcdata: Optional[GetdcdataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    divecomputerdump: List[DivecomputerdumpType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ExaminationType(IdType):
    class Meta:
        name = "examinationType"

    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    doctor: Optional[IndividualType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    link: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    examinationresult: Optional[ExaminationTypeExaminationresult] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    totallungcapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    vitalcapacity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class Gasdefinitions:
    class Meta:
        name = "gasdefinitions"
        namespace = "http://www.streit.cc/uddf/3.2/"

    mix: List[MixType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Generator(SimpleNamedType):
    class Meta:
        name = "generator"
        namespace = "http://www.streit.cc/uddf/3.2/"

    type: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    link: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    manufacturer: Optional[ManufacturerType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class InformationbeforediveType:
    class Meta:
        name = "informationbeforediveType"

    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divenumberofday: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    internaldivenumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    airtemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    surfaceintervalbeforedive: Optional[SurfaceintervalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    altitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    equipmentused: Optional["InformationbeforediveType.Equipmentused"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    apparatus: Optional[InformationbeforediveTypeApparatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    platform: Optional[InformationbeforediveTypePlatform] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    purpose: Optional[InformationbeforediveTypePurpose] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    stateofrestbeforedive: Optional[InformationbeforediveTypeStateofrestbeforedive] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tripmembership: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    alcoholbeforedive: Optional["InformationbeforediveType.Alcoholbeforedive"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    medicalbeforedive: Optional["InformationbeforediveType.Medicalbeforedive"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    nosuit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "length": 0,
        }
    )
    price: Optional[PriceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    inputprofile: Optional[InputprofileType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    plannedprofile: Optional[SamplesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    surfacepressure: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )

    @dataclass
    class Equipmentused:
        leadquantity: Optional[float] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )
        link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
            }
        )

    @dataclass
    class Alcoholbeforedive:
        drink: List[DrugType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Medicalbeforedive:
        medicine: List[DrugType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )


@dataclass
class InstructorType(IndividualType):
    class Meta:
        name = "instructorType"

    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class Maker:
    class Meta:
        name = "maker"
        namespace = "http://www.streit.cc/uddf/3.2/"

    manufacturer: List[ManufacturerType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Mediadata:
    class Meta:
        name = "mediadata"
        namespace = "http://www.streit.cc/uddf/3.2/"

    audio: List[MediaType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    image: List[ImageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    video: List[MediaType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PurchaseType:
    class Meta:
        name = "purchaseType"

    datetime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    price: Optional[PriceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    shop: Optional[ShopType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class SingleLifeFormType:
    class Meta:
        name = "singleLifeFormType"

    species: List[SpeciesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class SitedataType:
    class Meta:
        name = "sitedataType"

    arealength: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    areawidth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    averagevisibility: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bottom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    density: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    difficulty: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_inclusive": 1,
            "max_inclusive": 10,
        }
    )
    globallightintensity: Optional[GloballightintensityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    maximumdepth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    maximumvisibility: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    minimumdepth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    minimumvisibility: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    terrain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    wreck: List[WreckType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    cave: Optional[CaveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    indoor: Optional[IndoorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lake: Optional[PlaceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    river: Optional[PlaceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    shore: Optional[PlaceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class TrippartType(SimpleNamedType):
    class Meta:
        name = "trippartType"

    dateoftrip: Optional["TrippartType.Dateoftrip"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    geography: Optional[GeographyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    accomodation: Optional[AccommodationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    operator: Optional[OperatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    vessel: Optional[VesselType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    link: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    relateddives: Optional["TrippartType.Relateddives"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    pricedivepackage: Optional[PriceperdivepackageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    priceperdive: Optional[PriceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    rating: List[RatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Dateoftrip:
        startdate: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        enddate: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Relateddives:
        link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )


@dataclass
class CertificationType:
    class Meta:
        name = "certificationType"

    level: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    specialty: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    certificatenumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    organization: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    instructor: Optional[InstructorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    issuedate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    validdate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class EquipmentPieceType(NamedType):
    class Meta:
        name = "equipmentPieceType"

    link: Optional[LinkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    manufacturer: Optional[ManufacturerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    serialnumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    purchase: Optional[PurchaseType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    serviceinterval: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    nextservicedate: Optional[EncapsulatedDateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class FloraType:
    class Meta:
        name = "floraType"

    rhodophyceae: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    phaeophyceae: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    chlorophyceae: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    spermatophyta: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    floravarious: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class InvertebrataType:
    class Meta:
        name = "invertebrataType"

    porifera: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    coelenterata: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    cnidaria: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    ctenophora: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    plathelminthes: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    bryozoa: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    phoronidea: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    ascidiacea: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    echinodermata: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    mollusca: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    crustacea: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    invertebratavarious: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class TableType(BaseCalculationType):
    class Meta:
        name = "tableType"

    tablescope: Optional[TablescopeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class TripType(NamedType):
    class Meta:
        name = "tripType"

    rating: List[RatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    trippart: List[TrippartType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_occurs": 1,
        }
    )


@dataclass
class VertebrataType:
    class Meta:
        name = "vertebrataType"

    chondrichthyes: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    osteichthyes: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    mammalia: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    amphibia: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    reptilia: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    vertebratavarious: Optional[SingleLifeFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class CameraType(IdType):
    class Meta:
        name = "cameraType"

    body: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lens: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    housing: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    flash: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class Divetrip:
    class Meta:
        name = "divetrip"
        namespace = "http://www.streit.cc/uddf/3.2/"

    trip: List[TripType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class FaunaType:
    class Meta:
        name = "faunaType"

    invertebrata: Optional[InvertebrataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    vertebrata: Optional[VertebrataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class RebreatherType(EquipmentPieceType):
    class Meta:
        name = "rebreatherType"

    o2sensor: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class SuitType(EquipmentPieceType):
    class Meta:
        name = "suitType"

    suittype: Optional[SuitTypeSuittype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class Tablegeneration:
    class Meta:
        name = "tablegeneration"
        namespace = "http://www.streit.cc/uddf/3.2/"

    calculateprofile: Optional["Tablegeneration.Calculateprofile"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    calculatetable: Optional["Tablegeneration.Calculatetable"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    calculatebottomtimetable: Optional["Tablegeneration.Calculatebottomtimetable"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Calculateprofile:
        profile: List[BaseCalculationType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Calculatetable:
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Calculatebottomtimetable:
        bottomtimetable: List[BottomtimetableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )


@dataclass
class TankType(EquipmentPieceType):
    class Meta:
        name = "tankType"

    tankmaterial: Optional[TankmaterialType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tankvolume: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class VideocameraType(IdType):
    class Meta:
        name = "videocameraType"

    body: Optional[EquipmentPieceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lens: Optional[EquipmentPieceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    housing: Optional[EquipmentPieceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    light: Optional[EquipmentPieceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class EcologyType:
    class Meta:
        name = "ecologyType"

    fauna: Optional[FaunaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    flora: Optional[FloraType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class EquipmentType:
    class Meta:
        name = "equipmentType"

    boots: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    buoyancycontroldevice: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    camera: List[CameraType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    compass: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    compressor: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divecomputer: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    equipmentconfiguration: List[EquipmentconfigurationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    fins: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    gloves: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    knife: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lead: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    light: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    mask: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    rebreather: List[RebreatherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    regulator: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    scooter: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    suit: List[SuitType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    tank: List[TankType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    variouspieces: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    videocamera: List[VideocameraType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    watch: List[EquipmentPieceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class ObservationsType(EcologyType):
    class Meta:
        name = "observationsType"

    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class PersonType(IndividualType):
    class Meta:
        name = "personType"

    equipment: Optional[EquipmentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    medical: Optional["PersonType.Medical"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    education: Optional["PersonType.Education"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    divepermissions: Optional["PersonType.Divepermissions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    diveinsurances: Optional["PersonType.Diveinsurances"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )

    @dataclass
    class Medical:
        examination: List[ExaminationType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Education:
        certification: List[CertificationType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Divepermissions:
        permit: List[PermitType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Diveinsurances:
        insurance: List[InsuranceType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )


@dataclass
class SiteType(NamedType):
    class Meta:
        name = "siteType"

    environment: Optional[SiteTypeEnvironment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    geography: Optional[GeographyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    ecology: Optional[EcologyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    sitedata: Optional[SitedataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    rating: List[RatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )


@dataclass
class Diver:
    class Meta:
        name = "diver"
        namespace = "http://www.streit.cc/uddf/3.2/"

    owner: Optional[PersonType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    buddy: List["Diver.Buddy"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Buddy(PersonType):
        student: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )


@dataclass
class Divesite:
    class Meta:
        name = "divesite"
        namespace = "http://www.streit.cc/uddf/3.2/"

    divebase: List[DivebaseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    site: List[SiteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class InformationafterdiveType:
    class Meta:
        name = "informationafterdiveType"

    surfaceintervalafterdive: Optional[SurfaceintervalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    lowesttemperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    greatestdepth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    visibility: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    current: Optional[InformationafterdiveTypeCurrent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    diveplan: Optional[InformationafterdiveTypeDiveplan] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    equipmentmalfunction: Optional[InformationafterdiveTypeEquipmentmalfunction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    pressuredrop: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    problems: Optional[InformationafterdiveTypeProblems] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    program: Optional[InformationafterdiveTypeProgram] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    thermalcomfort: Optional[InformationafterdiveTypeThermalcomfort] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    workload: Optional[InformationafterdiveTypeWorkload] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    desaturationtime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    noflighttime: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    rating: Optional[RatingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    anysymptoms: Optional["InformationafterdiveType.Anysymptoms"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    diveduration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    divetable: Optional[InformationafterdiveTypeDivetable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    globalalarmsgiven: Optional["InformationafterdiveType.Globalalarmsgiven"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    highestpo2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    observations: Optional[ObservationsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    averagedepth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )

    @dataclass
    class Anysymptoms:
        notes: List[NotesType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Globalalarmsgiven:
        globalalarm: List[GlobalalarmsgivenGlobalalarm] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.streit.cc/uddf/3.2/",
                "min_occurs": 1,
            }
        )


@dataclass
class DiveType(IdType):
    class Meta:
        name = "diveType"

    applicationdata: Optional[ApplicationdataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    informationbeforedive: Optional[InformationbeforediveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )
    tankdata: List[TankdataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    samples: Optional[SamplesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
        }
    )
    informationafterdive: Optional[InformationafterdiveType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "required": True,
        }
    )


@dataclass
class RepetitiongroupType(IdType):
    class Meta:
        name = "repetitiongroupType"

    dive: List[DiveType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.streit.cc/uddf/3.2/",
            "min_occurs": 1,
        }
    )


@dataclass
class Profiledata:
    class Meta:
        name = "profiledata"
        namespace = "http://www.streit.cc/uddf/3.2/"

    repetitiongroup: List[RepetitiongroupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Uddf:
    class Meta:
        name = "uddf"
        namespace = "http://www.streit.cc/uddf/3.2/"

    generator: Optional[Generator] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    mediadata: Optional[Mediadata] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    maker: Optional[Maker] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    business: Optional[Business] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    diver: Optional[Diver] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    divesite: Optional[Divesite] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    divetrip: Optional[Divetrip] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    gasdefinitions: Optional[Gasdefinitions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    decomodel: Optional["Uddf.Decomodel"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    profiledata: Optional[Profiledata] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tablegeneration: Optional[Tablegeneration] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    divecomputercontrol: Optional[Divecomputercontrol] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Decomodel:
        buehlmann: Optional[BuehlmannType] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        rgbm: Optional[RgbmType] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        vpm: Optional[VpmType] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
