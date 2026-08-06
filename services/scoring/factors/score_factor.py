from abc import ABC
from abc import abstractmethod

from models.analysis.analysis_bundle import AnalysisBundle


class ScoreFactor(ABC):
    @abstractmethod
    def compute(
        self,
        analysis: AnalysisBundle,
    ) -> float:
        """
        Computes this factor contribution.

        Returns a value between 0 and 100.
        """
        raise NotImplementedError