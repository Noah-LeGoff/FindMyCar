from models.listing import Listing
from models.score import Score
from models.search import Search

from services.scoring.compatibility import CompatibilityScorer
from services.scoring.opportunity import OpportunityScorer
from services.scoring.weights import (
    COMPATIBILITY_WEIGHT,
    OPPORTUNITY_WEIGHT,
)


class ScoringService:

    def __init__(self) -> None:
        self._compatibility = CompatibilityScorer()
        self._opportunity = OpportunityScorer()

    def score(self, search: Search, listing: Listing) -> Score:

        compatibility = self._compatibility.compute(search, listing)
        opportunity = self._opportunity.compute(search, listing)

        total = (compatibility.score * COMPATIBILITY_WEIGHT + opportunity.compute * OPPORTUNITY_WEIGHT)

        return Score(
            compatibility=compatibility.score,
            opportunity=opportunity.score,
            total=total,
            breakdown=(
                compatibility.breakdowns
                + opportunity.breakdowns
            ),
        )