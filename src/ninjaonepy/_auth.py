import time

import httpx

TOKEN_URL_US = "https://app.ninjarmm.com/oauth/token"
TOKEN_URL_EU = "https://eu.ninjarmm.com/oauth/token"


class TokenManager:
    """Fetches and caches OAuth2 client-credentials tokens.

    Automatically refreshes the token 30 seconds before expiry.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        europe: bool = False,
        scopes: list[str] | None = None,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_url = TOKEN_URL_EU if europe else TOKEN_URL_US
        self._scopes = scopes or ["monitoring", "management", "control"]
        self._token: str | None = None
        self._expires_at: float = 0.0

    def get_token(self) -> str:
        if self._token and time.monotonic() < self._expires_at - 30:
            return self._token
        self._refresh()
        assert self._token is not None
        return self._token

    def _refresh(self) -> None:
        resp = httpx.post(
            self._token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self._client_id,
                "client_secret": self._client_secret,
                "scope": " ".join(self._scopes),
            },
        )
        resp.raise_for_status()
        payload = resp.json()
        self._token = payload["access_token"]
        self._expires_at = time.monotonic() + payload.get("expires_in", 3600)
