from models.listing import Listing


def test_create_listing():
    """
    Listing should store required information.
    """

    listing = Listing(
        source="test",
        title="BMW E36",
        brand="BMW",
        model="E36"
    )

    assert listing.brand == "BMW"
    assert listing.model == "E36"


def test_listing_default_values():
    """
    Listing should use correct defaults.
    """

    listing = Listing(
        source="test",
        title="BMW E36",
        brand="BMW",
        model="E36"
    )

    assert listing.price == 0
    assert listing.currency == "EUR"
    assert listing.score == 0
    assert listing.version is None


def test_listing_optional_fields():
    """
    Optional fields should accept values.
    """

    listing = Listing(
        source="test",
        title="BMW E36",
        brand="BMW",
        model="E36",
        year=1995,
        mileage=150000
    )

    assert listing.year == 1995
    assert listing.mileage == 150000