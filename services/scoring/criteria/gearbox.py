from models.listing import Listing
from models.search import Search

from services.scoring.criteria.exact_match import ExactMatchCriterion


class GearboxCriterion(ExactMatchCriterion):
    DISPLAY_NAME = "Gearbox"

    MAX_POINTS = 10

    MISSING_SEARCH_REASON = "No gearbox specified."
    MISSING_LISTING_REASON = "Gearbox unavailable."

    MATCH_REASON = "Gearbox matches the search."
    MISMATCH_REASON = "Gearbox does not match the search."

    def _get_search_value(
        self,
        search: Search,
    ):
        return search.gearbox

    def _get_listing_value(
        self,
        listing: Listing,
    ):
        return listing.gearbox