from models.listing import Listing
from models.opportunity_context import OpportunityContext
from models.partial_score import PartialScore
from models.search import Search

from services.scoring.opportunity_criteria import OPPORTUNITY_CRITERIA


class OpportunityScorer:
    """
    Computes the opportunity score of a listing.
    """

    def compute(
        self,
        search: Search,
        listing: Listing,
        context: OpportunityContext | None = None,
    ) -> PartialScore:
        """
        Computes the opportunity score.
        """

        context = context or OpportunityContext()

        breakdowns = [
            criterion.evaluate(
                search,
                listing,
                context,
            )
            for criterion in OPPORTUNITY_CRITERIA
        ]

        return PartialScore(
            score=sum(
                breakdown.points
                for breakdown in breakdowns
            ),
            breakdowns=breakdowns,
        )