from abc import ABC, abstractmethod

from models.listing import Listing
from models.search import Search
from models.score_breakdown import ScoreBreakdown


class ScoringCriterion(ABC):
    """
    Base class for all scoring criteria.
    """

    @abstractmethod
    def evaluate(
        self,
        search: Search,
        listing: Listing,
    ) -> ScoreBreakdown:
        """
        Computes the contribution of this criterion.
        """
        raise NotImplementedError