from models.listing import Listing
from models.search import Search

from services.scoring.criteria.exact_match import ExactMatchCriterion


class FuelCriterion(ExactMatchCriterion):
    DISPLAY_NAME = "Fuel"

    MAX_POINTS = 10

    MISSING_SEARCH_REASON = "No fuel specified."
    MISSING_LISTING_REASON = "Fuel unavailable."

    MATCH_REASON = "Fuel matches the search."
    MISMATCH_REASON = "Fuel does not match the search."

    def _get_search_value(
        self,
        search: Search,
    ):
        return search.fuel

    def _get_listing_value(
        self,
        listing: Listing,
    ):
        return listing.fuel