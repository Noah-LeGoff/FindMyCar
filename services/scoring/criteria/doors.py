from models.listing import Listing
from models.search import Search

from services.scoring.criteria.exact_match import ExactMatchCriterion


class DoorsCriterion(ExactMatchCriterion):
    DISPLAY_NAME = "Doors"

    MAX_POINTS = 8

    MISSING_SEARCH_REASON = "No door count specified."
    MISSING_LISTING_REASON = "Door count unavailable."

    MATCH_REASON = "Door count matches the search."
    MISMATCH_REASON = "Door count does not match the search."

    def _search_value(
        self,
        search: Search,
    ):
        return search.doors

    def _listing_value(
        self,
        listing: Listing,
    ):
        return listing.doors