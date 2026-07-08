from dataclasses import dataclass


@dataclass(slots=True)
class ScoreBreakdown:
    """
    Represents the contribution of a scoring criterion.
    """

    criterion: str

    points: float

    max_points: float

    reason: str