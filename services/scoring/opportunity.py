from models.listing import Listing
from models.partial_score import PartialScore
from models.search import Search


class OpportunityScorer:
    """
    Computes the opportunity score.
    """

    def compute(self, search: Search, listing: Listing) -> PartialScore:
        return PartialScore()