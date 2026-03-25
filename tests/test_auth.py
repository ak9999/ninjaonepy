import pytest
from pytest_httpx import HTTPXMock

from ninjaonepy import Client
from ninjaonepy._auth import TokenManager
from ninjaonepy._exceptions import AuthError


def test_token_fetch(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://app.ninjarmm.com/oauth/token",
        json={"access_token": "abc123", "expires_in": 3600},
    )
    tm = TokenManager(client_id="x", client_secret="y")
    assert tm.get_token() == "abc123"


def test_token_cached(httpx_mock: HTTPXMock) -> None:
    """Second call must not make a second HTTP request."""
    httpx_mock.add_response(
        url="https://app.ninjarmm.com/oauth/token",
        json={"access_token": "abc123", "expires_in": 3600},
    )
    tm = TokenManager(client_id="x", client_secret="y")
    tm.get_token()
    tm.get_token()  # no second mock registered — would raise if a request were made


def test_eu_token_url(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://eu.ninjarmm.com/oauth/token",
        json={"access_token": "eu-token", "expires_in": 3600},
    )
    tm = TokenManager(client_id="x", client_secret="y", europe=True)
    assert tm.get_token() == "eu-token"


def test_auth_error_propagates(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://app.ninjarmm.com/oauth/token",
        json={"access_token": "tok", "expires_in": 3600},
    )
    httpx_mock.add_response(
        url="https://app.ninjarmm.com/v2/organizations",
        status_code=401,
        json={"error": "Unauthorized"},
    )
    with pytest.raises(AuthError), Client(client_id="bad", client_secret="creds") as client:
        client.get_organizations()


def test_client_repr() -> None:
    # __repr__ reads base_url only — no HTTP call, no mock needed
    with Client(client_id="x", client_secret="y") as client:
        assert "app.ninjarmm.com" in repr(client)


def test_client_eu_base_url() -> None:
    with Client(client_id="x", client_secret="y", europe=True) as client:
        assert "eu.ninjarmm.com" in repr(client)
