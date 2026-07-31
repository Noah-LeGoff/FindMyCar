from dataclasses import dataclass

from models.analysis.ai_analysis import AIAnalysis
from models.analysis.maintenance_analysis import MaintenanceAnalysis
from models.analysis.price_analysis import PriceAnalysis
from models.analysis.recommendation import Recommendation
from models.analysis.reliability_analysis import ReliabilityAnalysis
from models.analysis.safety_analysis import SafetyAnalysis
from models.analysis.technical_analysis import TechnicalAnalysis
from models.listing import Listing
from models.score import Score


@dataclass(frozen=True)
class CompleteAnalysis:
    listing: Listing
    score: Score

    technical: TechnicalAnalysis
    reliability: ReliabilityAnalysis
    price: PriceAnalysis
    maintenance: MaintenanceAnalysis
    safety: SafetyAnalysis
    ai: AIAnalysis

    recommendations: tuple[Recommendation, ...] = ()