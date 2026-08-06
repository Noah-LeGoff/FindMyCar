from services.analysis.analyzers.analyzer import Analyzer

from models.analysis.maintenance_analysis import MaintenanceAnalysis
from models.listing import Listing
from models.search import Search


class MaintenanceAnalyzer(Analyzer):
    result_key = "maintenance"

    def analyze(
        self,
        search: Search,
        listing: Listing,
    ) -> MaintenanceAnalysis:
        return MaintenanceAnalysis(
            summary="Not implemented",
        )