from dataclasses import dataclass

from models.analysis.ai_analysis import AIAnalysis
from models.analysis.analysis_result import AnalysisResult
from models.analysis.maintenance_analysis import MaintenanceAnalysis
from models.analysis.price_analysis import PriceAnalysis
from models.analysis.reliability_analysis import ReliabilityAnalysis
from models.analysis.safety_analysis import SafetyAnalysis
from models.analysis.technical_analysis import TechnicalAnalysis


@dataclass(frozen=True)
class AnalysisBundle:
    technical: TechnicalAnalysis
    reliability: ReliabilityAnalysis
    price: PriceAnalysis
    maintenance: MaintenanceAnalysis
    safety: SafetyAnalysis
    ai: AIAnalysis

    @classmethod
    def from_results(
        cls,
        results: dict[str, AnalysisResult],
    ) -> "AnalysisBundle":
        return cls(
            technical=results["technical"],
            reliability=results["reliability"],
            price=results["price"],
            maintenance=results["maintenance"],
            safety=results["safety"],
            ai=results["ai"],
        )