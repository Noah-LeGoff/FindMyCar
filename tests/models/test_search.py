from models.search import Search


def test_create_empty_search():
    """
    Search should be created with default values.
    """

    search = Search(
        id=None,
        user_id=1
    )

    assert search.user_id == 1
    assert search.brand is None
    assert search.max_price is None


def test_create_search_with_filters():
    """
    Search should store provided filters.
    """

    search = Search(
        id=None,
        user_id=1,
        brand="BMW",
        model="E36",
        max_price=10000,
        max_mileage=200000
    )

    assert search.brand == "BMW"
    assert search.model == "E36"
    assert search.max_price == 10000
    assert search.max_mileage == 200000


def test_search_keywords_defaults():
    """
    Keywords should default to empty tuples.
    """

    search = Search(
        id=None,
        user_id=1
    )

    assert search.include_keywords == ()
    assert search.exclude_keywords == ()