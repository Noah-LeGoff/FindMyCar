from dataclasses import dataclass

from models.score.score_breakdown import ScoreBreakdown

from models.enums import Recommendation


@dataclass(slots=True)
class FinalScore:
    """
    Represents the final score of a listing.
    """

    total: float

    compatibility: float

    opportunity: float

    compatibility_breakdowns: list[ScoreBreakdown]

    opportunity_breakdowns: list[ScoreBreakdown]

    @property
    def recommendation(self) -> Recommendation:
        """
        Returns a recommendation based on the total score.
        """

        if self.total >= 95:
            return Recommendation.EXCEPTIONAL

        if self.total >= 85:
            return Recommendation.EXCELLENT

        if self.total >= 70:
            return Recommendation.VERY_INTERESTING

        if self.total >= 55:
            return Recommendation.WORTH_CONSIDERING

        if self.total >= 40:
            return Recommendation.LOW_INTEREST

        return Recommendation.AVOID