from models.analysis_result import AnalysisResult

from services.ai.description_analyzer import DescriptionAnalyzer
from services.ai.prompt_builder import PromptBuilder
from services.ai.providers.fake import FakeAIProvider
from services.scoring.opportunity_criteria.description_ai import (
    DescriptionAICriterion,
)

from tests.factories import make_listing, make_search


def make_criterion():
    analyzer = DescriptionAnalyzer(
        FakeAIProvider(),
        PromptBuilder(),
    )

    return DescriptionAICriterion(analyzer)


def test_returns_zero_when_description_missing():
    criterion = make_criterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(description=None),
    )

    assert result.points == 0


def test_returns_zero_when_no_ai_signal():
    criterion = make_criterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(description="BMW E36"),
    )

    assert result.points == 0


def test_reason_is_description_unavailable():
    criterion = make_criterion()

    result = criterion.evaluate(
        make_search(),
        make_listing(description=None),
    )

    assert result.reason == "Description unavailable."