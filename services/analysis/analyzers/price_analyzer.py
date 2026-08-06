from services.analysis.analyzers.analyzer import Analyzer

from models.analysis.price_analysis import PriceAnalysis
from models.listing import Listing
from models.search import Search


class PriceAnalyzer(Analyzer):
    result_key = "price"

    def analyze(
        self,
        search: Search,
        listing: Listing,
    ) -> PriceAnalysis:
        return PriceAnalysis(
            summary="Not implemented",
        )