from dataclasses import dataclass, field

from models.score_breakdown import ScoreBreakdown


@dataclass(slots=True)
class PartialScore:
    """
    Represents the result of a scoring computation.
    """

    score: float = 0

    breakdowns: list[ScoreBreakdown] = field(default_factory=list)