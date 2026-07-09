from models.listing import Listing
from models.score_breakdown import ScoreBreakdown
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class YearCriterion(ScoringCriterion):

    DISPLAY_NAME = "Year"
    MAX_POINTS = 10

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ) -> ScoreBreakdown:

        return self._build_breakdown(
            points=0,
            reason="Not implemented yet.",
        )