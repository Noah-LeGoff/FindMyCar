from models.listing import Listing
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class GearboxCriterion(ScoringCriterion):
    """
    Scores a listing based on its gearbox.
    """

    DISPLAY_NAME = "Gearbox"

    MAX_POINTS = 10

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ):

        if search.gearbox is None:
            return self._build_breakdown(
                self.MAX_POINTS,
                "No gearbox specified.",
            )

        if listing.gearbox is None:
            return self._build_breakdown(
                0,
                "Gearbox unavailable.",
            )

        if listing.gearbox == search.gearbox:
            return self._build_breakdown(
                self.MAX_POINTS,
                "Gearbox matches the search.",
            )

        return self._build_breakdown(
            0,
            "Gearbox does not match the search.",
        )