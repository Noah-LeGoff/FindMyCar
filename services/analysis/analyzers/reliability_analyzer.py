from services.analysis.analyzers.analyzer import Analyzer

from models.analysis.reliability_analysis import ReliabilityAnalysis
from models.listing import Listing
from models.search import Search


class ReliabilityAnalyzer(Analyzer):
    result_key = "reliability"

    def analyze(
        self,
        search: Search,
        listing: Listing,
    ) -> ReliabilityAnalysis:
        return ReliabilityAnalysis(
            summary="Not implemented",
        )