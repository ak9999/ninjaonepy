from pytest_httpx import HTTPXMock

from ninjaonepy import Client

MOCK_ORGS = [
    {"id": 1, "name": "Acme Corp"},
    {"id": 2, "name": "Globex"},
]

MOCK_DEVICES = [
    {"id": 101, "organizationId": 1, "nodeClass": "WINDOWS_SERVER", "systemName": "DC01"},
]

MOCK_ALERTS = [
    {"uid": "abc-123", "deviceId": 101, "message": "Disk space low"},
]


def test_get_organizations(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/organizations",
        json=MOCK_ORGS,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_organizations()
    assert result == MOCK_ORGS


def test_get_organizations_pagination(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/organizations?pageSize=1",
        json=[MOCK_ORGS[0]],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_organizations(page_size=1)
    assert len(result) == 1  # type: ignore[arg-type]


def test_get_devices(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/devices",
        json=MOCK_DEVICES,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_devices()
    assert isinstance(result, list)
    assert result[0]["systemName"] == "DC01"  # type: ignore[index]


def test_get_devices_detailed(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/devices-detailed",
        json=MOCK_DEVICES,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_devices_detailed()
    assert isinstance(result, list)


def test_get_alerts(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/alerts",
        json=MOCK_ALERTS,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_alerts()
    assert result == MOCK_ALERTS


def test_get_users(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/users",
        json=[{"id": 1, "name": "Alice", "userType": "TECHNICIAN"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_users()
    assert isinstance(result, list)


def test_get_policies(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/policies",
        json=[{"id": 1, "name": "Default Policy"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_policies()
    assert isinstance(result, list)


def test_get_locations(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/locations",
        json=[{"id": 10, "organizationId": 1, "name": "HQ"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_locations()
    assert isinstance(result, list)
