from models.listing import Listing
from models.search import Search

from services.scoring.comparison_mode import ComparisonMode
from services.scoring.criteria.numeric import NumericCriterion


class PriceCriterion(NumericCriterion):
    DISPLAY_NAME = "Price"

    MAX_POINTS = 25

    COMPARISON_MODE = ComparisonMode.MAXIMUM

    MISSING_VALUE_REASON = "Price unavailable."
    MISSING_LIMIT_REASON = "No maximum budget specified."

    WITHIN_LIMIT_REASON = "Price within budget."
    WITHIN_TOLERANCE_REASON = "Price within tolerance"

    EXCEEDS_LIMIT_REASON = "Price exceeds budget by"
    EXCEEDS_MAX_REASON = "Price exceeds maximum accepted budget"

    INVALID_VALUE_REASON = "Invalid listing price."

    def _listing_value(
        self,
        listing: Listing,
    ):
        return listing.price

    def _search_limit(
        self,
        search: Search,
    ):
        return search.max_price
    
    def _is_valid_value(
        self,
        value: int |float,
    ) -> bool:
        return value > 1