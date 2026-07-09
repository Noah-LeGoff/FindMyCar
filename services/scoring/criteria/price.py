from models.listing import Listing
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class PriceCriterion(ScoringCriterion):
    """
    Scores a listing according to the user's maximum budget.
    """

    DISPLAY_NAME = "Price"

    MAX_POINTS = 25

    TOLERANCE = 0.05
    MAX_OVER_BUDGET = 0.30

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ):
        """
        Evaluates the listing price against the user's budget.
        """

        if listing.price is None:
            return self._build_breakdown(
                0,
                "Price unavailable.",
            )

        if listing.price <= 1:
            return self._build_breakdown(
                0,
                "Invalid listing price.",
            )

        if search.max_price is None:
            return self._build_breakdown(
                self.MAX_POINTS,
                "No maximum budget specified.",
            )

        if listing.price <= search.max_price:
            return self._build_breakdown(
                self.MAX_POINTS,
                "Price within budget.",
            )

        over_budget_ratio = (
            listing.price - search.max_price
        ) / search.max_price

        if over_budget_ratio <= self.TOLERANCE:
            return self._build_breakdown(
                self.MAX_POINTS,
                (
                    "Price within tolerance "
                    f"(+{self._format_ratio(over_budget_ratio)})."
                ),
            )

        if over_budget_ratio >= self.MAX_OVER_BUDGET:
            return self._build_breakdown(
                0,
                (
                    "Price exceeds maximum accepted budget "
                    f"(+{self._format_ratio(over_budget_ratio)})."
                ),
            )

        normalized = (
            over_budget_ratio - self.TOLERANCE
        ) / (
            self.MAX_OVER_BUDGET - self.TOLERANCE
        )

        points = self.MAX_POINTS * (1 - normalized)

        return self._build_breakdown(
            points,
            (
                "Price exceeds budget by "
                f"{self._format_ratio(over_budget_ratio)}."
            ),
        )