from models.scored_listing import ScoredListing


class RankingService:
    """
    Sorts scored listings by descending final score.
    """

    def rank(
        self,
        listings: list[ScoredListing],
    ) -> list[ScoredListing]:
        """
        Returns the listings sorted by descending score.
        """

        return sorted(
            listings,
            key=lambda listing: listing.score.total,
            reverse=True,
        )