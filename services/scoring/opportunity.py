from models.listing import Listing
from models.partial_score import PartialScore
from models.search import Search

from services.scoring.criteria import OPPORTUNITY_CRITERIA


class OpportunityScorer:
    """
    Computes the opportunity score of a listing.
    """

    def compute(
        self,
        search: Search,
        listing: Listing,
    ) -> PartialScore:
        """
        Computes the opportunity score.
        """

        breakdowns = [
            criterion.evaluate(search, listing)
            for criterion in OPPORTUNITY_CRITERIA
        ]

        return PartialScore(
            score=sum(
                breakdown.points
                for breakdown in breakdowns
            ),
            breakdowns=breakdowns,
        )