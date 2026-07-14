from models.listing import Listing
from models.search import Search

from services.scoring.comparison_mode import ComparisonMode
from services.scoring.criteria.numeric import NumericCriterion


class MileageCriterion(NumericCriterion):
    DISPLAY_NAME = "Mileage"

    MAX_POINTS = 20

    COMPARISON_MODE = ComparisonMode.MAXIMUM

    MISSING_VALUE_REASON = "Mileage unavailable."
    MISSING_LIMIT_REASON = "No maximum mileage specified."

    WITHIN_LIMIT_REASON = "Mileage within limit."
    WITHIN_TOLERANCE_REASON = "Mileage within tolerance"

    EXCEEDS_LIMIT_REASON = "Mileage exceeds limit by"
    EXCEEDS_MAX_REASON = "Mileage exceeds maximum accepted limit"

    def _listing_value(
        self,
        listing: Listing,
    ):
        return listing.mileage

    def _search_limit(
        self,
        search: Search,
    ):
        return search.max_mileage