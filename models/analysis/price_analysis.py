from dataclasses import dataclass

from models.analysis.analysis_result import AnalysisResult


@dataclass(frozen=True)
class PriceAnalysis(AnalysisResult):
    estimated_price: int = 0
    difference: int = 0