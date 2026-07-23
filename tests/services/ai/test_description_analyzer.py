from models.analysis_result import AnalysisResult

from services.ai.description_analyzer import DescriptionAnalyzer
from services.ai.providers.fake import FakeAIProvider


def test_returns_analysis_result():
    analyzer = DescriptionAnalyzer(
        FakeAIProvider(),
    )

    result = analyzer.analyze(
        "BMW E36",
    )

    assert isinstance(result, AnalysisResult)


def test_returns_empty_analysis():
    analyzer = DescriptionAnalyzer(
        FakeAIProvider(),
    )

    result = analyzer.analyze(
        "BMW E36",
    )

    assert result == AnalysisResult()