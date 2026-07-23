from abc import ABC, abstractmethod

from models.analysis_result import AnalysisResult


class AIProvider(ABC):
    """
    Base interface implemented by every AI provider.
    """

    @abstractmethod
    def analyze(
        self,
        prompt: str,
    ) -> AnalysisResult:
        """
        Sends a prompt to an AI model and returns structured analysis.
        """
        raise NotImplementedError