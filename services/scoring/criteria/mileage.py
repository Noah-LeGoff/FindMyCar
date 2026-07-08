from models.listing import Listing
from models.score_breakdown import ScoreBreakdown
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class MileageCriterion(ScoringCriterion):

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ) -> ScoreBreakdown:

        return ScoreBreakdown(
            criterion="Mileage",
            points=0,
            max_points=15,
            reason="Not implemented yet",
        )