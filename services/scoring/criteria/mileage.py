from models.listing import Listing
from models.score_breakdown import ScoreBreakdown
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class MileageCriterion(ScoringCriterion):

    DISPLAY_NAME = "Mileage"
    MAX_POINTS = 15

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ) -> ScoreBreakdown:

        return self._build_breakdown(
            points=0,
            reason="Not implemented yet.",
        )