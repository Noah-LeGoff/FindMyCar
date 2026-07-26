from models.final_score import FinalScore
from models.partial_score import PartialScore


class ScoreAggregator:
    """
    Combines compatibility and opportunity scores into a final score.
    """

    COMPATIBILITY_MAX_SCORE = 75
    OPPORTUNITY_MAX_SCORE = 75

    FINAL_COMPATIBILITY_WEIGHT = 75
    FINAL_OPPORTUNITY_WEIGHT = 25

    def aggregate(
        self,
        compatibility: PartialScore,
        opportunity: PartialScore,
    ) -> FinalScore:
        """
        Aggregates partial scores into a final score.
        """

        compatibility_score = self._normalize(
            compatibility.score,
            self.COMPATIBILITY_MAX_SCORE,
            self.FINAL_COMPATIBILITY_WEIGHT,
        )

        opportunity_score = self._normalize(
            opportunity.score,
            self.OPPORTUNITY_MAX_SCORE,
            self.FINAL_OPPORTUNITY_WEIGHT,
        )

        total = compatibility_score + opportunity_score

        return FinalScore(
            total=round(total),
            compatibility=round(compatibility_score),
            opportunity=round(opportunity_score),
            compatibility_breakdowns=compatibility.breakdowns,
            opportunity_breakdowns=opportunity.breakdowns,
        )

    @staticmethod
    def _normalize(
        score: float,
        max_score: float,
        weight: float,
    ) -> float:
        """
        Normalizes a score to its contribution to the final score.
        """

        if max_score <= 0:
            return 0

        return (score / max_score) * weight