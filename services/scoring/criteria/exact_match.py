from abc import abstractmethod

from models.listing import Listing
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class ExactMatchCriterion(ScoringCriterion):
    """
    Base class for criteria requiring an exact value match.
    """

    MISSING_SEARCH_REASON = "No value specified."
    MISSING_LISTING_REASON = "Value unavailable."

    MATCH_REASON = "Matches the search."
    MISMATCH_REASON = "Does not match the search."

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ):
        search_value = self._get_search_value(search)

        if search_value is None:
            return self._build_breakdown(
                self.MAX_POINTS,
                self.MISSING_SEARCH_REASON,
            )

        listing_value = self._get_listing_value(listing)

        if listing_value is None:
            return self._build_breakdown(
                0,
                self.MISSING_LISTING_REASON,
            )

        if listing_value == search_value:
            return self._build_breakdown(
                self.MAX_POINTS,
                self.MATCH_REASON,
            )

        return self._build_breakdown(
            0,
            self.MISMATCH_REASON,
        )

    @abstractmethod
    def _get_search_value(
        self,
        search: Search,
    ):
        raise NotImplementedError

    @abstractmethod
    def _get_listing_value(
        self,
        listing: Listing,
    ):
        raise NotImplementedError