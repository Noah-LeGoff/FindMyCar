from dataclasses import dataclass


@dataclass(frozen=True)
class Recommendation:
    title: str
    description: str
    severity: int