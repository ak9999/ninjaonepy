import pytest
from pytest_httpx import HTTPXMock

TOKEN_RESPONSE = {
    "access_token": "test-access-token",
    "token_type": "Bearer",
    "expires_in": 3600,
}


@pytest.fixture
def auth_mock(httpx_mock: HTTPXMock) -> HTTPXMock:
    """Mocks the OAuth token endpoint. Use in any test that constructs a Client."""
    httpx_mock.add_response(
        url="https://app.ninjarmm.com/oauth/token",
        json=TOKEN_RESPONSE,
    )
    return httpx_mock
