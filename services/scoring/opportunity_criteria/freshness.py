from datetime import date

from models.listing import Listing
from models.opportunity_context import OpportunityContext
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class FreshnessCriterion(ScoringCriterion):
    """
    Scores a listing according to its publication date.
    """

    DISPLAY_NAME = "Freshness"

    MAX_POINTS = 20

    MAX_AGE_DAYS = 90

    def __init__(
        self,
        today: date | None = None,
    ):
        self._today = today or date.today()

    def evaluate(
        self,
        search: Search,
        listing: Listing,
        context: OpportunityContext,
    ):
        if listing.published_at is None:
            return self._build_breakdown(
                0,
                "Publication date unavailable.",
            )

        published_date = listing.published_at.date()

        age = (self._today - published_date).days

        if age <= 0:
            return self._build_breakdown(
                self.MAX_POINTS,
                "Published today.",
            )

        if age >= self.MAX_AGE_DAYS:
            return self._build_breakdown(
                0,
                "Listing is too old.",
            )

        ratio = age / self.MAX_AGE_DAYS

        points = self.MAX_POINTS * (1 - ratio)

        return self._build_breakdown(
            points,
            f"Published {self._format_days(age)} ago.",
        )