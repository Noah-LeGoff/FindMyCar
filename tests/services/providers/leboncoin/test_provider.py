import pytest
import requests

from core.exceptions import ProviderError

from services.providers.leboncoin.provider import LeboncoinProvider

from tests.factories import make_search


def test_build_payload_empty_search():
    provider = LeboncoinProvider()

    payload = provider._build_payload(
        make_search(
            brand=None,
            model=None,
            min_price=None,
            max_price=None,
            min_year=None,
            max_year=None,
            max_mileage=None,
        )
    )

    assert payload == {}


def test_build_payload_contains_filters():
    provider = LeboncoinProvider()

    payload = provider._build_payload(
        make_search(
            brand="BMW",
            model="E36",
            min_price=5000,
            max_price=10000,
            min_year=1995,
            max_year=1999,
            max_mileage=180000,
        )
    )

    assert payload == {
        "brand": "BMW",
        "model": "E36",
        "min_price": 5000,
        "max_price": 10000,
        "min_year": 1995,
        "max_year": 1999,
        "max_mileage": 180000,
    }


def test_fetch_results_returns_json(mocker):
    provider = LeboncoinProvider()

    fake_response = mocker.Mock()

    fake_response.json.return_value = {
        "ads": [
            {
                "title": "BMW E36",
            }
        ]
    }

    fake_response.raise_for_status.return_value = None

    post = mocker.patch(
        "requests.post",
        return_value=fake_response,
    )

    payload = {
        "brand": "BMW",
    }

    result = provider._fetch_results(
        "https://example.com",
        payload,
    )

    post.assert_called_once_with(
        "https://example.com",
        json=payload,
        headers=None,
        timeout=10,
    )

    assert result == {
        "ads": [
            {
                "title": "BMW E36",
            }
        ]
    }


def test_fetch_results_raises_provider_error_on_connection_error(
    mocker,
):
    provider = LeboncoinProvider()

    mocker.patch(
        "requests.post",
        side_effect=requests.ConnectionError,
    )

    with pytest.raises(
        ProviderError,
    ):
        provider._fetch_results(
            "https://example.com",
            {},
        )


def test_fetch_results_raises_provider_error_on_http_error(
    mocker,
):
    provider = LeboncoinProvider()

    response = mocker.Mock()

    response.raise_for_status.side_effect = (
        requests.HTTPError
    )

    mocker.patch(
        "requests.post",
        return_value=response,
    )

    with pytest.raises(
        ProviderError,
    ):
        provider._fetch_results(
            "https://example.com",
            {},
        )