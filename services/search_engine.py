from providers.demo_provider import DemoProvider


class SearchEngine:

    def __init__(self):

        self.providers = [

            DemoProvider()

        ]

    def run(self, search):

        listings = []

        for provider in self.providers:

            listings.extend(
                provider.search(search)
            )

        from services.scoring_service import ScoringService

        scoring = ScoringService()

        for listing in listings:

            listing.score = scoring.score(listing)

        interesting = []

        for listing in listings:

            if listing.score >= 60:

                interesting.append(listing)

        return interesting