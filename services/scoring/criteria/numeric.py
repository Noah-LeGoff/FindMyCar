from abc import abstractmethod

from models.listing import Listing
from models.search import Search

from services.scoring.comparison_mode import ComparisonMode
from services.scoring.criteria.base import ScoringCriterion


class NumericCriterion(ScoringCriterion):
    """
    Base class for numeric scoring criteria.
    """

    COMPARISON_MODE = ComparisonMode.MAXIMUM

    TOLERANCE = 0.05
    MAX_OVER_LIMIT = 0.30

    MISSING_VALUE_REASON = ""
    MISSING_LIMIT_REASON = ""

    WITHIN_LIMIT_REASON = ""
    WITHIN_TOLERANCE_REASON = ""

    EXCEEDS_LIMIT_REASON = ""
    EXCEEDS_MAX_REASON = ""

    INVALID_VALUE_REASON = "Invalid value."

    @abstractmethod
    def _listing_value(
        self,
        listing: Listing,
    ) -> int | float | None:
        pass

    @abstractmethod
    def _search_limit(
        self,
        search: Search,
    ) -> int | float | None:
        pass

    def _is_valid_value(
        self,
        value: int | float,
    ) -> bool:
        """
        Returns whether the listing value is valid.
        """

        return True

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ):
        value = self._listing_value(listing)
        limit = self._search_limit(search)

        if value is None:
            return self._build_breakdown(
                0,
                self.MISSING_VALUE_REASON,
            )
        
        if not self._is_valid_value(value):
            return self._build_breakdown(
                0,
                self.INVALID_VALUE_REASON,
            )

        if limit is None:
            return self._build_breakdown(
                self.MAX_POINTS,
                self.MISSING_LIMIT_REASON,
            )

        if self.COMPARISON_MODE == ComparisonMode.MAXIMUM:
            difference_ratio = (value - limit) / limit

            if value <= limit:
                return self._build_breakdown(
                    self.MAX_POINTS,
                    self.WITHIN_LIMIT_REASON,
                )

        else:
            difference_ratio = (limit - value) / limit

            if value >= limit:
                return self._build_breakdown(
                    self.MAX_POINTS,
                    self.WITHIN_LIMIT_REASON,
                )

        if difference_ratio <= self.TOLERANCE:
            return self._build_breakdown(
                self.MAX_POINTS,
                (
                    f"{self.WITHIN_TOLERANCE_REASON} "
                    f"(+{self._format_ratio(difference_ratio)})."
                ),
            )

        if difference_ratio >= self.MAX_OVER_LIMIT:
            return self._build_breakdown(
                0,
                (
                    f"{self.EXCEEDS_MAX_REASON} "
                    f"(+{self._format_ratio(difference_ratio)})."
                ),
            )

        normalized = (
            difference_ratio - self.TOLERANCE
        ) / (
            self.MAX_OVER_LIMIT - self.TOLERANCE
        )

        points = self.MAX_POINTS * (1 - normalized)

        return self._build_breakdown(
            points,
            (
                f"{self.EXCEEDS_LIMIT_REASON} "
                f"{self._format_ratio(difference_ratio)}."
            ),
        )