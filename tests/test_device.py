from pytest_httpx import HTTPXMock

from ninjaonepy import Client

MOCK_DEVICE = {
    "id": 101,
    "organizationId": 1,
    "nodeClass": "WINDOWS_SERVER",
    "systemName": "DC01",
}


def test_get_device(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101",
        json=MOCK_DEVICE,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_device(101)
    assert result == MOCK_DEVICE


def test_get_device_disks(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101/disks",
        json=[{"model": "Samsung SSD", "capacity": 512000}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_device_disks(101)
    assert isinstance(result, list)


def test_get_device_volumes(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101/volumes",
        json=[{"name": "C:", "capacity": 512000, "freeSpace": 200000}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_device_volumes(101)
    assert isinstance(result, list)


def test_get_device_software(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101/software",
        json=[{"name": "7-Zip", "version": "22.01"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_device_software(101)
    assert isinstance(result, list)


def test_get_device_os_patches(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101/os-patches",
        json=[{"id": 1001, "title": "Security Update", "severity": "CRITICAL"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_device_os_patches(101)
    assert isinstance(result, list)


def test_get_device_windows_services(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101/windows-services",
        json=[{"name": "wuauserv", "state": "RUNNING"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_device_windows_services(101)
    assert isinstance(result, list)


def test_get_device_alerts(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101/alerts",
        json=[{"uid": "abc-123", "message": "Disk space low"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_device_alerts(101)
    assert isinstance(result, list)


def test_get_device_active_jobs(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101/jobs",
        json=[{"id": 9001, "type": "PATCH"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_device_active_jobs(101)
    assert isinstance(result, list)
