from models.final_score import FinalScore

from services.ranking.ranking_service import RankingService
from services.scoring.scoring_engine import ScoringEngine

from tests.factories import make_listing, make_search


def test_pipeline_scores_single_listing():
    engine = ScoringEngine()

    result = engine.compute(
        make_search(),
        make_listing(),
    )

    assert isinstance(
        result,
        FinalScore,
    )

    assert 0 <= result.total <= 100

def test_pipeline_scores_multiple_listings():
    engine = ScoringEngine()

    listings = [
        make_listing(),
        make_listing(),
        make_listing(),
    ]

    result = engine.compute_all(
        make_search(),
        listings,
    )

    assert len(result) == 3

    assert all(
        isinstance(
            scored.score,
            FinalScore,
        )
        for scored in result
    )


def test_pipeline_ranks_scored_listings():
    engine = ScoringEngine()
    ranking = RankingService()

    listings = [
        make_listing(),
        make_listing(),
        make_listing(),
    ]

    scored = engine.compute_all(
        make_search(),
        listings,
    )

    ranked = ranking.rank(
        scored,
    )

    assert len(ranked) == len(scored)

    assert all(
        ranked[i].score.total >= ranked[i + 1].score.total
        for i in range(len(ranked) - 1)
    )


def test_pipeline_preserves_breakdowns():
    engine = ScoringEngine()

    result = engine.compute(
        make_search(),
        make_listing(),
    )

    assert result.compatibility_breakdowns is not None
    assert result.opportunity_breakdowns is not None


def test_pipeline_scores_are_always_between_zero_and_one_hundred():
    engine = ScoringEngine()

    listings = [
        make_listing(),
        make_listing(),
        make_listing(),
        make_listing(),
        make_listing(),
    ]

    results = engine.compute_all(
        make_search(),
        listings,
    )

    assert all(
        0 <= scored.score.total <= 100
        for scored in results
    )