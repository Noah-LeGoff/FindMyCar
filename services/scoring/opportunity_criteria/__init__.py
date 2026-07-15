from services.scoring.opportunity_criteria.freshness import FreshnessCriterion
from services.scoring.opportunity_criteria.price_opportunity import (
    PriceOpportunityCriterion,
)

OPPORTUNITY_CRITERIA = [
    FreshnessCriterion(),
    PriceOpportunityCriterion(),
]