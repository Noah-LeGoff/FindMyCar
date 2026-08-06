from abc import ABC
from abc import abstractmethod

from models.analysis.analysis_result import AnalysisResult
from models.listing import Listing
from models.search import Search


class Analyzer(ABC):
    """
    Base interface implemented by every analysis module.
    """

    result_key: str

    @abstractmethod
    def analyze(
        self,
        search: Search,
        listing: Listing,
    ) -> AnalysisResult:
        """
        Analyze a listing according to the current search.

        Returns the corresponding AnalysisResult.
        """
        raise NotImplementedError