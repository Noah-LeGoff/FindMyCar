from dataclasses import dataclass

from models.analysis.recommendation import Recommendation


@dataclass(frozen=True)
class AnalysisResult:
    summary: str
    recommendations: tuple[Recommendation, ...] = ()