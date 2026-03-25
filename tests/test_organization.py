from pytest_httpx import HTTPXMock

from ninjaonepy import Client

MOCK_ORG = {"id": 1, "name": "Acme Corp", "locations": []}

MOCK_CONTACTS = [
    {"id": 5, "firstName": "Alice", "lastName": "Smith", "email": "alice@acme.com"},
]


def test_get_organization(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/organization/1",
        json=MOCK_ORG,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_organization(1)
    assert result == MOCK_ORG


def test_get_organization_devices(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/organization/1/devices",
        json=[{"id": 101, "systemName": "DC01"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_organization_devices(1)
    assert isinstance(result, list)


def test_get_organization_locations(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/organization/1/locations",
        json=[{"id": 10, "name": "HQ"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_organization_locations(1)
    assert isinstance(result, list)


def test_get_organization_end_users(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/organization/1/end-users",
        json=[{"id": 20, "name": "Bob"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_organization_end_users(1)
    assert isinstance(result, list)


def test_get_contacts(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/contacts",
        json=MOCK_CONTACTS,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_contacts()
    assert result == MOCK_CONTACTS


def test_get_contact(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/contact/5",
        json=MOCK_CONTACTS[0],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_contact(5)
    assert result["email"] == "alice@acme.com"  # type: ignore[index]


def test_get_organization_custom_fields(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/organization/1/custom-fields",
        json={"ticketingEmail": "help@acme.com"},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_organization_custom_fields(1)
    assert isinstance(result, dict)
