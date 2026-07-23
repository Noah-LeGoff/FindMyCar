from models.analysis_result import AnalysisResult

from services.ai.prompt_builder import PromptBuilder
from services.ai.providers.base import AIProvider


class DescriptionAnalyzer:
    """
    Orchestrates the AI description analysis workflow.
    """

    def __init__(
        self,
        provider: AIProvider,
        prompt_builder: PromptBuilder | None = None,
    ) -> None:
        self._provider = provider
        self._prompt_builder = prompt_builder or PromptBuilder()

    def analyze(
        self,
        description: str,
    ) -> AnalysisResult:
        """
        Analyzes a vehicle description.
        """

        prompt = self._prompt_builder.build(description)

        return self._provider.analyze(prompt)