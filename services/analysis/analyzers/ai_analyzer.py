from services.analysis.analyzers.analyzer import Analyzer

from models.analysis.ai_analysis import AIAnalysis
from models.listing import Listing
from models.search import Search


class AIAnalyzer(Analyzer):
    result_key = "ai"

    def analyze(
        self,
        search: Search,
        listing: Listing,
    ) -> AIAnalysis:
        return AIAnalysis(
            summary="Not implemented",
        )