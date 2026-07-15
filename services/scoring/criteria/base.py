from abc import ABC, abstractmethod

from models.listing import Listing
from models.score_breakdown import ScoreBreakdown
from models.search import Search


class ScoringCriterion(ABC):
    """
    Base class for all scoring criteria.
    """

    DISPLAY_NAME: str = ""
    MAX_POINTS: float = 0

    @abstractmethod
    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ) -> ScoreBreakdown:
        """
        Evaluates a listing for this criterion.
        """
        raise NotImplementedError

    def _build_breakdown(
        self,
        points: float,
        reason: str,
    ) -> ScoreBreakdown:
        """
        Creates a ScoreBreakdown for this criterion.
        """

        return ScoreBreakdown(
            criterion=self.DISPLAY_NAME,
            points=max(0, min(points, self.MAX_POINTS)),
            max_points=self.MAX_POINTS,
            reason=reason,
        )

    def _format_ratio(
        self,
        ratio: float,
    ) -> str:
        """
        Formats a ratio as a percentage with one decimal place.
        """

        return f"{ratio * 100:.1f}%"
    
    def _format_days(
        self,
        days: int,
    ) -> str:
        """
        Formats a duration expressed in days.
        """

        if days == 1:
            return "1 day"

        return f"{days} days"