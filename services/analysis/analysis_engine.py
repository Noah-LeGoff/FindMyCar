from services.analysis.analyzers.analyzer import Analyzer

from models.analysis.analysis_bundle import AnalysisBundle
from models.listing import Listing
from models.search import Search


class AnalysisEngine:
    def __init__(
        self,
        analyzers: tuple[Analyzer, ...],
    ):
        self._analyzers = analyzers

    def analyze(
        self,
        search: Search,
        listing: Listing,
    ) -> AnalysisBundle:
        results = {}

        for analyzer in self._analyzers:
            results[analyzer.result_key] = analyzer.analyze(
                search,
                listing,
            )

        return AnalysisBundle.from_results(results)