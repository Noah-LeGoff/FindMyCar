from dataclasses import dataclass, field

from models.listing import Listing


@dataclass(slots=True)
class OpportunityContext:
    """
    Additional data required by opportunity criteria.
    """

    comparable_listings: list[Listing] = field(default_factory=list)