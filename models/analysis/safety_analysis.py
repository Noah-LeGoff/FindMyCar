from dataclasses import dataclass

from models.analysis.analysis_result import AnalysisResult


@dataclass(frozen=True)
class SafetyAnalysis(AnalysisResult):
    pass