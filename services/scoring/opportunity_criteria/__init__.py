from services.scoring.opportunity_criteria.freshness import FreshnessCriterion
from services.scoring.opportunity_criteria.price_opportunity import (
    PriceOpportunityCriterion,
)
from services.scoring.opportunity_criteria.rarity import (
    RarityCriterion,
)

OPPORTUNITY_CRITERIA = [
    FreshnessCriterion(),
    PriceOpportunityCriterion(),
    RarityCriterion(),
]