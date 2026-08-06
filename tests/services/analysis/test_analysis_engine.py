from unittest.mock import Mock, patch

from models.analysis.analysis_bundle import AnalysisBundle
from models.analysis.analysis_result import AnalysisResult
from services.analysis.analysis_engine import AnalysisEngine
from services.analysis.analyzers.analyzer import Analyzer

from tests.factories import (
    make_listing,
    make_search,
)


def make_analyzer(result_key: str):
    analyzer = Mock(spec=Analyzer)
    analyzer.result_key = result_key
    analyzer.analyze.return_value = Mock(spec=AnalysisResult)
    return analyzer


def test_calls_every_analyzer():
    search = make_search()
    listing = make_listing()

    analyzers = (
        make_analyzer("technical"),
        make_analyzer("reliability"),
        make_analyzer("price"),
        make_analyzer("maintenance"),
        make_analyzer("safety"),
        make_analyzer("ai"),
    )

    engine = AnalysisEngine(analyzers)

    with patch.object(
        AnalysisBundle,
        "from_results",
        return_value=Mock(spec=AnalysisBundle),
    ):
        engine.analyze(search, listing)

    for analyzer in analyzers:
        analyzer.analyze.assert_called_once_with(search, listing)


def test_builds_analysis_bundle_from_results():
    search = make_search()
    listing = make_listing()

    analyzers = (
        make_analyzer("technical"),
        make_analyzer("reliability"),
        make_analyzer("price"),
        make_analyzer("maintenance"),
        make_analyzer("safety"),
        make_analyzer("ai"),
    )

    engine = AnalysisEngine(analyzers)

    expected_results = {
        analyzer.result_key: analyzer.analyze.return_value
        for analyzer in analyzers
    }

    with patch.object(
        AnalysisBundle,
        "from_results",
        return_value=Mock(spec=AnalysisBundle),
    ) as from_results:
        engine.analyze(search, listing)

    from_results.assert_called_once_with(expected_results)


def test_returns_analysis_bundle():
    search = make_search()
    listing = make_listing()

    expected_bundle = Mock(spec=AnalysisBundle)

    engine = AnalysisEngine(())

    with patch.object(
        AnalysisBundle,
        "from_results",
        return_value=expected_bundle,
    ):
        result = engine.analyze(search, listing)

    assert result is expected_bundle


def test_supports_empty_analyzer_collection():
    search = make_search()
    listing = make_listing()

    engine = AnalysisEngine(())

    with patch.object(
        AnalysisBundle,
        "from_results",
        return_value=Mock(spec=AnalysisBundle),
    ) as from_results:
        engine.analyze(search, listing)

    from_results.assert_called_once_with({})