from models.analysis_result import AnalysisResult

from services.ai.description_analyzer import DescriptionAnalyzer
from services.ai.providers.fake import FakeAIProvider


def test_returns_analysis_result():
    provider = FakeAIProvider()

    result = provider.analyze("Any prompt")

    assert isinstance(result, AnalysisResult)


def test_returns_empty_analysis():
    provider = FakeAIProvider()

    result = provider.analyze("Any prompt")

    assert result == AnalysisResult()


def test_prompt_is_built_and_sent_to_provider():
    provider = FakeAIProvider()

    analyzer = DescriptionAnalyzer(provider)

    analyzer.analyze("BMW E36")

    assert "BMW E36" in provider.last_prompt