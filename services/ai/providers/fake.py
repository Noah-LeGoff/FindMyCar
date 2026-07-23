from models.analysis_result import AnalysisResult

from services.ai.providers.base import AIProvider


class FakeAIProvider(AIProvider):
    """
    Fake AI provider used for development and unit testing.
    """
    
    def __init__(self):
        self.last_prompt = None

    def analyze(
        self,
        prompt: str,
    ) -> AnalysisResult:

        self.last_prompt = prompt

        return AnalysisResult()