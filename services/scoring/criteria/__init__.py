from services.scoring.criteria.mileage import MileageCriterion
from services.scoring.criteria.price import PriceCriterion
from services.scoring.criteria.year import YearCriterion
from services.scoring.criteria.fuel import FuelCriterion
from services.scoring.criteria.gearbox import GearboxCriterion

COMPATIBILITY_CRITERIA = (
    PriceCriterion(),
    MileageCriterion(),
    YearCriterion(),
    FuelCriterion()
)