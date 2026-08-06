from services.analysis.analyzers.analyzer import Analyzer

from models.analysis.technical_analysis import TechnicalAnalysis
from models.listing import Listing
from models.search import Search


class TechnicalAnalyzer(Analyzer):
    result_key = "technical"

    def analyze(
        self,
        search: Search,
        listing: Listing,
    ) -> TechnicalAnalysis:
        return TechnicalAnalysis(
            summary="Not implemented",
        )