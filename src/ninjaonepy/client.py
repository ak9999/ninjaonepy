from ._auth import TokenManager
from ._http import HttpClient
from .backup import BackupMixin
from .custom_fields import CustomFieldsMixin
from .device import DeviceMixin
from .groups import GroupsMixin
from .management import ManagementMixin
from .organization import OrganizationMixin
from .queries import QueriesMixin
from .system import SystemMixin
from .ticketing import TicketingMixin
from .vulnerability import VulnerabilityMixin


class Client(
    SystemMixin,
    OrganizationMixin,
    DeviceMixin,
    GroupsMixin,
    QueriesMixin,
    ManagementMixin,
    TicketingMixin,
    BackupMixin,
    CustomFieldsMixin,
    VulnerabilityMixin,
):
    """NinjaOne API v2 client.

    Usage:
        client = Client(client_id="...", client_secret="...")
        orgs = client.get_organizations()

        # Or as a context manager:
        with Client(client_id="...", client_secret="...") as client:
            orgs = client.get_organizations()

    Args:
        client_id: OAuth2 client ID from the NinjaOne admin portal.
        client_secret: OAuth2 client secret.
        europe: Set True to target the EU data centre endpoints.
        timeout: HTTP request timeout in seconds. Default is 30.
        scopes: OAuth2 scopes to request. Defaults to all three:
                ["monitoring", "management", "control"].
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        europe: bool = False,
        timeout: float = 30.0,
        scopes: list[str] | None = None,
    ) -> None:
        tokens = TokenManager(client_id, client_secret, europe, scopes)
        self._http = HttpClient(tokens, europe, timeout)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def __repr__(self) -> str:
        base = self._http._client.base_url
        return f"{type(self).__name__}(base_url={str(base)!r})"
