from models.scored_listing import ScoredListing
from models.search import Search

from services.ranking.ranking_service import RankingService
from services.repository.listing_repository import ListingRepository
from services.scoring.scoring_engine import ScoringEngine


class SearchPipeline:
    """
    Executes a complete search pipeline.
    """

    def __init__(
        self,
        repository: ListingRepository,
        scoring_engine: ScoringEngine,
        ranking_service: RankingService,
    ):
        self._repository = repository
        self._scoring_engine = scoring_engine
        self._ranking_service = ranking_service

    def execute(
        self,
        search: Search,
    ) -> list[ScoredListing]:
        """
        Executes a complete search.
        """

        listings = self._repository.search(search)

        scored = self._scoring_engine.compute_all(
            search,
            listings,
        )

        return self._ranking_service.rank(scored)