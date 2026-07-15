from statistics import median

from models.listing import Listing
from models.opportunity_context import OpportunityContext
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class PriceOpportunityCriterion(ScoringCriterion):
    """
    Scores a listing according to its price compared to the current market.
    """

    DISPLAY_NAME = "Price Opportunity"

    MAX_POINTS = 30

    MIN_SAMPLE_SIZE = 10

    MAX_BONUS_DIFFERENCE = 0.20

    def evaluate(
        self,
        search: Search,
        listing: Listing,
        context: OpportunityContext,
    ):
        """
        Evaluates the opportunity score based on market prices.

        The implementation is intentionally incremental.
        Market analysis will be added in subsequent steps.
        """

        comparable_prices = [
            comparable.price
            for comparable in context.comparable_listings
            if comparable.price is not None
            and comparable.price > 1
        ]

        if len(comparable_prices) < self.MIN_SAMPLE_SIZE:
            return self._build_breakdown(
                0,
                "Market sample too small.",
            )

        market_median = median(comparable_prices)

        if listing.price is None:
            return self._build_breakdown(
                0,
                "Listing price unavailable.",
            )

        if listing.price <= 1:
            return self._build_breakdown(
                0,
                "Invalid listing price.",
            )

        difference = (
            market_median - listing.price
        ) / market_median

        if difference <= 0:
            return self._build_breakdown(
                0,
                "Price is above market median.",
            )

        points = (
            difference
            / self.MAX_BONUS_DIFFERENCE
        ) * self.MAX_POINTS

        points = min(
            points,
            self.MAX_POINTS,
        )

        return self._build_breakdown(
            points,
            (
                f"Price is "
                f"{difference:.1%} below market median."
            ),
        )