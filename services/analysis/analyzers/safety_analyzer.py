from services.analysis.analyzers.analyzer import Analyzer

from models.analysis.safety_analysis import SafetyAnalysis
from models.listing import Listing
from models.search import Search


class SafetyAnalyzer(Analyzer):
    result_key = "safety"

    def analyze(
        self,
        search: Search,
        listing: Listing,
    ) -> SafetyAnalysis:
        return SafetyAnalysis(
            summary="Not implemented",
        )