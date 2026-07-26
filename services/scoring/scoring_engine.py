from models.final_score import FinalScore
from models.listing import Listing
from models.scored_listing import ScoredListing
from models.search import Search

from services.scoring.compatibility import CompatibilityScorer
from services.scoring.opportunity import OpportunityScorer
from services.scoring.score_aggregator import ScoreAggregator


class ScoringEngine:
    """
    Computes the final score of one or more listings.
    """

    def __init__(
        self,
        compatibility_scorer: CompatibilityScorer | None = None,
        opportunity_scorer: OpportunityScorer | None = None,
        aggregator: ScoreAggregator | None = None,
    ) -> None:
        self._compatibility = (
            compatibility_scorer
            or CompatibilityScorer()
        )

        self._opportunity = (
            opportunity_scorer
            or OpportunityScorer()
        )

        self._aggregator = (
            aggregator
            or ScoreAggregator()
        )

    def compute(
        self,
        search: Search,
        listing: Listing,
    ) -> FinalScore:
        """
        Computes the final score of a single listing.
        """

        compatibility = self._compatibility.compute(
            search,
            listing,
        )

        opportunity = self._opportunity.compute(
            search,
            listing,
        )

        return self._aggregator.aggregate(
            compatibility,
            opportunity,
        )

    def compute_all(
        self,
        search: Search,
        listings: list[Listing],
    ) -> list[ScoredListing]:
        """
        Computes the final score of multiple listings.
        """

        return [
            ScoredListing(
                listing=listing,
                score=self.compute(
                    search,
                    listing,
                ),
            )
            for listing in listings
        ]