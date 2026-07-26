from enum import Enum


class FuelType(Enum):
    GASOLINE = "gasoline"
    DIESEL = "diesel"
    HYBRID = "hybrid"
    PLUG_IN_HYBRID = "plug_in_hybrid"
    ELECTRIC = "electric"
    LPG = "lpg"
    CNG = "cng"


class GearboxType(Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    SEMI_AUTOMATIC = "semi_automatic"


class Recommendation(Enum):
    EXCEPTIONAL = "Exceptional choice"
    EXCELLENT = "Excellent choice"
    VERY_INTERESTING = "Very interesting"
    WORTH_CONSIDERING = "Worth considering"
    LOW_INTEREST = "Low interest"
    AVOID = "Avoid"