from services.pipeline.search_pipeline import SearchPipeline
from services.providers.fake_listing_provider import FakeListingProvider
from services.ranking.ranking_service import RankingService
from services.repository.listing_repository import ListingRepository
from services.scoring.scoring_engine import ScoringEngine

from tests.factories import make_listing, make_search


def make_pipeline() -> SearchPipeline:
    provider = FakeListingProvider(
        [
            make_listing(price=10000),
            make_listing(price=8000),
            make_listing(price=12000),
        ]
    )

    repository = ListingRepository(provider)

    return SearchPipeline(
        repository=repository,
        scoring_engine=ScoringEngine(),
        ranking_service=RankingService(),
    )


def test_execute_returns_all_results():
    pipeline = make_pipeline()

    results = pipeline.execute(
        make_search(),
    )

    assert len(results) == 3


def test_execute_returns_ranked_results():
    pipeline = make_pipeline()

    results = pipeline.execute(
        make_search(),
    )

    assert all(
        results[i].score.total >= results[i + 1].score.total
        for i in range(len(results) - 1)
    )


def test_execute_returns_scored_listings():
    pipeline = make_pipeline()

    results = pipeline.execute(
        make_search(),
    )

    assert all(
        hasattr(result, "score")
        for result in results
    )