from dataclasses import dataclass

from models.analysis.analysis_result import AnalysisResult


@dataclass(frozen=True)
class ReliabilityAnalysis(AnalysisResult):
    score: float = 0.0