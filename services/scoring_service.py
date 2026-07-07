class ScoringService:

    def score(self, listing):

        score = 0

        # Prix
        if listing.price < 8000:
            score += 30

        # Kilométrage
        if listing.mileage < 200000:
            score += 20

        # Description
        keywords = [
            "factures",
            "entretien",
            "origine",
            "première main",
            "carnet"
        ]

        text = listing.description.lower()

        for word in keywords:

            if word in text:
                score += 10

        return min(score, 100)