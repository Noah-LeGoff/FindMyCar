from models.listing import Listing
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class MileageCriterion(ScoringCriterion):
    """
    Scores a listing according to the user's maximum mileage.
    """

    DISPLAY_NAME = "Mileage"

    MAX_POINTS = 20

    TOLERANCE = 0.05
    MAX_OVER_LIMIT = 0.30

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ):
        """
        Evaluates the listing mileage against the user's maximum mileage.
        """

        if listing.mileage is None:
            return self._build_breakdown(
                0,
                "Mileage unavailable.",
            )

        if search.max_mileage is None:
            return self._build_breakdown(
                self.MAX_POINTS,
                "No maximum mileage specified.",
            )

        if listing.mileage <= search.max_mileage:
            return self._build_breakdown(
                self.MAX_POINTS,
                "Mileage within limit.",
            )

        over_limit_ratio = (
            listing.mileage - search.max_mileage
        ) / search.max_mileage

        if over_limit_ratio <= self.TOLERANCE:
            return self._build_breakdown(
                self.MAX_POINTS,
                (
                    "Mileage within tolerance "
                    f"(+{self._format_ratio(over_limit_ratio)})."
                ),
            )

        if over_limit_ratio >= self.MAX_OVER_LIMIT:
            return self._build_breakdown(
                0,
                (
                    "Mileage exceeds maximum accepted limit "
                    f"(+{self._format_ratio(over_limit_ratio)})."
                ),
            )

        normalized = (
            over_limit_ratio - self.TOLERANCE
        ) / (
            self.MAX_OVER_LIMIT - self.TOLERANCE
        )

        points = self.MAX_POINTS * (1 - normalized)

        return self._build_breakdown(
            points,
            (
                "Mileage exceeds limit by "
                f"{self._format_ratio(over_limit_ratio)}."
            ),
        )