from typing import Any

import httpx

from ._auth import TokenManager
from ._exceptions import AuthError, NinjaError, NotFoundError, RateLimitError

BASE_US = "https://app.ninjarmm.com"
BASE_EU = "https://eu.ninjarmm.com"

JsonResponse = dict[str, Any] | list[Any]


def _clean(params: dict[str, Any] | None) -> dict[str, Any] | None:
    """Strip None values so they are not serialised as query string parameters."""
    if params is None:
        return None
    return {k: v for k, v in params.items() if v is not None}


class HttpClient:
    """Thin httpx wrapper that injects auth headers and dispatches errors."""

    def __init__(
        self,
        token_manager: TokenManager,
        europe: bool = False,
        timeout: float = 30.0,
    ) -> None:
        self._tokens = token_manager
        self._client = httpx.Client(
            base_url=BASE_EU if europe else BASE_US,
            timeout=timeout,
        )

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._tokens.get_token()}",
            "Accept": "application/json",
        }

    def get(self, path: str, params: dict[str, Any] | None = None) -> JsonResponse:
        resp = self._client.get(path, params=_clean(params), headers=self._headers())
        return self._handle(resp)

    def post(self, path: str, json: JsonResponse | None = None) -> JsonResponse:
        resp = self._client.post(path, json=json, headers=self._headers())
        return self._handle(resp)

    def patch(self, path: str, json: dict[str, Any] | None = None) -> JsonResponse:
        resp = self._client.patch(path, json=_clean(json), headers=self._headers())
        return self._handle(resp)

    def delete(self, path: str) -> None:
        resp = self._client.delete(path, headers=self._headers())
        if resp.status_code not in (200, 204):
            self._handle(resp)

    @staticmethod
    def _handle(resp: httpx.Response) -> JsonResponse:
        match resp.status_code:
            case 200 | 201:
                return resp.json()  # type: ignore[no-any-return]
            case 204:
                return {}
            case 401:
                raise AuthError("Unauthorized — check client_id and client_secret")
            case 403:
                raise AuthError(f"Forbidden — missing OAuth scope for {resp.url}")
            case 404:
                raise NotFoundError(str(resp.url))
            case 429:
                raise RateLimitError("Rate limit exceeded")
            case _:
                raise NinjaError(f"HTTP {resp.status_code}: {resp.text[:200]}")

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "HttpClient":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
