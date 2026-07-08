from models.listing import Listing
from models.partial_score import PartialScore
from models.search import Search

from services.scoring.criteria import COMPATIBILITY_CRITERIA


class CompatibilityScorer:
    """
    Computes the compatibility score of a listing.
    """

    def compute(self, search: Search, listing: Listing) -> PartialScore:
        """
        Computes the compatibility score.
        """

        breakdowns = [
            criterion.evaluate(search, listing)
            for criterion in COMPATIBILITY_CRITERIA
        ]

        total = sum(
            breakdown.points
            for breakdown in breakdowns
        )

        return PartialScore(
            score=total,
            breakdowns=breakdowns,
        )