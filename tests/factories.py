from models.enums import FuelType, GearboxType
from models.listing import Listing
from models.opportunity_context import OpportunityContext
from models.search import Search


def make_search(**kwargs) -> Search:
    """
    Creates a Search object with sensible defaults.
    """

    data = {
        "id": 1,
        "user_id": 1,
        "brand": None,
        "model": None,
        "version": None,
        "min_price": None,
        "max_price": 10000,
        "min_year": None,
        "max_year": None,
        "max_mileage": 150000,
        "fuel": None,
        "gearbox": None,
        "doors": None,
        "latitude": None,
        "longitude": None,
        "radius_km": None,
        "include_keywords": (),
        "exclude_keywords": (),
        "created_at": None,
    }

    data.update(kwargs)

    return Search(**data)


def make_listing(**kwargs) -> Listing:
    """
    Creates a Listing object with sensible defaults.
    """

    data = {
        "source": "Leboncoin",
        "title": "BMW E36",
        "brand": "BMW",
        "model": "E36",
        "version": None,
        "year": 2018,
        "price": 10000,
        "currency": "EUR",
        "mileage": 100000,
        "fuel": FuelType.GASOLINE,
        "gearbox": GearboxType.MANUAL,
        "doors": 3,
        "location": "Rennes",
        "latitude": None,
        "longitude": None,
        "url": "",
        "image_url": None,
        "description": "",
        "published_at": None,
        "score": 0,
    }

    data.update(kwargs)

    return Listing(**data)


def make_market(
    *prices: int,
) -> OpportunityContext:
    """
    Creates an OpportunityContext populated with comparable listings.
    """

    listings = [
        make_listing(price=price)
        for price in prices
    ]

    return OpportunityContext(
        comparable_listings=listings,
    )