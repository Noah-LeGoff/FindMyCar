from services.providers.listing_provider import ListingProvider


class ProviderFactory:

    @staticmethod
    def create() -> ListingProvider:
        raise NotImplementedError