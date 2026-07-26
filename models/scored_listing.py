from dataclasses import dataclass

from models.final_score import FinalScore
from models.listing import Listing


@dataclass(slots=True)
class ScoredListing:
    """
    Associates a listing with its final score.
    """

    listing: Listing

    score: FinalScore