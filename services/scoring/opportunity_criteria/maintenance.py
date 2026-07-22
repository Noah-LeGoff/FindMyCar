from models.listing import Listing
from models.opportunity_context import OpportunityContext
from models.search import Search

from services.scoring.criteria.base import ScoringCriterion


class MaintenanceCriterion(ScoringCriterion):
    """
    Scores a listing according to the maintenance information found
    in its description.
    """

    DISPLAY_NAME = "Maintenance"

    MAX_POINTS = 20

    MAINTENANCE_ITEMS = (
        (
            8,
            (
                "distribution",
                "timing belt",
                "courroie de distribution",
                "kit distribution",
            ),
            "Timing belt replaced.",
        ),
        (
            6,
            (
                "embrayage",
                "clutch",
                "kit embrayage",
            ),
            "Clutch replaced.",
        ),
        (
            2,
            (
                "vidange",
                "oil change",
            ),
            "Recent oil change.",
        ),
        (
            2,
            (
                "révision",
                "service",
            ),
            "Recent service.",
        ),
        (
            3,
            (
                "factures",
                "maintenance invoices",
            ),
            "Maintenance invoices available.",
        ),
        (
            3,
            (
                "carnet d'entretien",
                "service book",
            ),
            "Service book available.",
        ),
        (
            2,
            (
                "contrôle technique",
                "technical inspection",
                "ct ok",
                "ct vierge",
            ),
            "Technical inspection available.",
        ),
        (
            2,
            (
                "freins neufs",
                "new brakes",
            ),
            "New brakes.",
        ),
        (
            2,
            (
                "pneus neufs",
                "new tires",
            ),
            "New tires.",
        ),
    )

    def evaluate(
        self,
        search: Search,
        listing: Listing,
        context: OpportunityContext,
    ):
        """
        Evaluates maintenance information contained in the listing
        description.
        """

        if not listing.description:
            return self._build_breakdown(
                0,
                "No description available.",
            )

        description = listing.description.lower()

        points = 0
        detected_items = []

        for (
            item_points,
            keywords,
            reason,
        ) in self.MAINTENANCE_ITEMS:

            if any(
                keyword in description
                for keyword in keywords
            ):
                points += item_points
                detected_items.append(reason)

        points = min(
            points,
            self.MAX_POINTS,
        )

        if not detected_items:
            return self._build_breakdown(
                0,
                "No maintenance information found.",
            )

        return self._build_breakdown(
            points,
            ", ".join(detected_items),
        )