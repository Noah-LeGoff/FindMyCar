from dataclasses import dataclass, field

from models.score_breakdown import ScoreBreakdown


@dataclass(slots=True)
class Score:
    """
    Represents the final score of a listing.
    """

    compatibility: float = 0

    opportunity: float = 0

    total: float = 0

    breakdown: list[ScoreBreakdown] = field(default_factory=list)

@property
def percentage(self) -> int:
    """Returns the rounded total score."""

    return round(self.total)