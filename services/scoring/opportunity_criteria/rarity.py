from models.listing import Listing
from models.opportunity_context import OpportunityContext
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class RarityCriterion(ScoringCriterion):
    """
    Scores a listing according to the number of comparable listings available.
    """

    DISPLAY_NAME = "Rarity"

    MAX_POINTS = 20

    RARITY_LEVELS = (
        (10, 20, "Vehicle is very rare on the market."),
        (20, 15, "Vehicle is rare on the market."),
        (50, 10, "Vehicle is uncommon on the market."),
        (100, 5, "Vehicle is fairly common on the market."),
    )

    def evaluate(
        self,
        search: Search,
        listing: Listing,
        context: OpportunityContext,
    ):
        """
        Evaluates the rarity of a listing.
        """

        comparable_count = len(
            context.comparable_listings
        )

        if comparable_count == 0:
            return self._build_breakdown(
                0,
                "No comparable listings available.",
            )

        for (
            max_count,
            points,
            reason,
        ) in self.RARITY_LEVELS:
            if comparable_count <= max_count:
                return self._build_breakdown(
                    points,
                    reason,
                )

        return self._build_breakdown(
            0,
            "Vehicle is very common on the market.",
        )