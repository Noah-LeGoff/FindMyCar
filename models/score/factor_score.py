from dataclasses import dataclass


@dataclass(frozen=True)
class FactorScore:
    """
    Represents the contribution of a single score factor.
    """

    name: str
    score: float
    explanation: str