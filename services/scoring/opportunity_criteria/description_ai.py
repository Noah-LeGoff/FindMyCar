from models.listing import Listing
from models.search import Search

from services.ai.description_analyzer import DescriptionAnalyzer
from services.scoring.criteria.base import ScoringCriterion


class DescriptionAICriterion(ScoringCriterion):
    """
    Scores a listing using AI analysis.

    The current implementation is intentionally simple.
    Business rules will be progressively introduced in future iterations.
    """

    DISPLAY_NAME = "AI Description"

    MAX_POINTS = 15

    def __init__(
        self,
        analyzer: DescriptionAnalyzer,
    ) -> None:
        self._analyzer = analyzer

    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ):
        description = listing.description

        if not description:
            return self._build_breakdown(
                0,
                "Description unavailable.",
            )

        analysis = self._analyzer.analyze(description)

        if analysis.confidence == 0:
            return self._build_breakdown(
                0,
                "No AI signals detected.",
            )

        return self._build_breakdown(
            self.MAX_POINTS,
            "AI analysis available.",
        )