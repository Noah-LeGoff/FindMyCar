from services.scoring.criteria.mileage import MileageCriterion
from services.scoring.criteria.price import PriceCriterion
from services.scoring.criteria.year import YearCriterion

COMPATIBILITY_CRITERIA = (
    PriceCriterion(),
    MileageCriterion(),
    YearCriterion(),
)