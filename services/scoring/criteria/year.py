from models.listing import Listing
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class YearCriterion(ScoringCriterion):
    """
    Scores a listing based on its production year.
    """

    DISPLAY_NAME = "Year"

    MAX_POINTS = 15

    TOLERANCE_YEARS = 1

    MAX_YEAR_GAP = 5

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ):
        if listing.year is None:
            return self._build_breakdown(
                0,
                "Year unavailable.",
            )

        if search.min_year is None:
            return self._build_breakdown(
                self.MAX_POINTS,
                "No minimum year specified.",
            )

        if listing.year >= search.min_year:
            return self._build_breakdown(
                self.MAX_POINTS,
                "Year meets the requirement.",
            )

        gap = search.min_year - listing.year

        if gap <= self.TOLERANCE_YEARS:
            return self._build_breakdown(
                self.MAX_POINTS,
                "Year within tolerance.",
            )

        if gap >= self.MAX_YEAR_GAP:
            return self._build_breakdown(
                0,
                f"Vehicle is {gap} years older than requested.",
            )

        normalized = (
            gap - self.TOLERANCE_YEARS
        ) / (
            self.MAX_YEAR_GAP - self.TOLERANCE_YEARS
        )

        points = self.MAX_POINTS * (1 - normalized)

        return self._build_breakdown(
            points,
            f"Vehicle is {gap} years older than requested.",
        )