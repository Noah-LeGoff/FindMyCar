from models.listing import Listing
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class FuelCriterion(ScoringCriterion):
    """
    Scores a listing based on its fuel type.
    """

    DISPLAY_NAME = "Fuel"

    MAX_POINTS = 10

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ):

        if search.fuel is None:
            return self._build_breakdown(
                self.MAX_POINTS,
                "No fuel specified.",
            )

        if listing.fuel is None:
            return self._build_breakdown(
                0,
                "Fuel unavailable.",
            )

        if listing.fuel == search.fuel:
            return self._build_breakdown(
                self.MAX_POINTS,
                "Fuel matches the search.",
            )

        return self._build_breakdown(
            0,
            "Fuel does not match the search.",
        )