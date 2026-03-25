from pytest_httpx import HTTPXMock

from ninjaonepy import Client


def test_get_antivirus_threats(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/antivirus-threats",
        json={"results": [{"deviceId": 101, "threatName": "Trojan.Gen"}], "cursor": None},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_antivirus_threats()
    assert isinstance(result, dict)


def test_get_antivirus_status(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/antivirus-status",
        json={"results": [{"deviceId": 101, "productState": "ON"}], "cursor": None},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_antivirus_status()
    assert isinstance(result, dict)


def test_get_operating_systems(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/operating-systems",
        json={"results": [{"deviceId": 101, "name": "Windows Server 2019"}], "cursor": None},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_operating_systems()
    assert isinstance(result, dict)


def test_get_disk_drives(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/disks",
        json={"results": [{"deviceId": 101, "model": "Samsung SSD"}], "cursor": None},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_disk_drives()
    assert isinstance(result, dict)


def test_get_installed_os_patches(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/os-patch-installs",
        json={"results": [{"deviceId": 101, "title": "KB5001234", "status": "INSTALLED"}]},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_installed_os_patches()
    assert isinstance(result, dict)


def test_get_last_logged_on_users(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/logged-on-users?pageSize=1000",
        json={"results": [{"deviceId": 101, "userName": "DOMAIN\\alice"}], "cursor": None},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_last_logged_on_users()
    assert isinstance(result, dict)


def test_get_windows_services(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/windows-services",
        json={"results": [{"deviceId": 101, "name": "wuauserv", "state": "RUNNING"}]},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_windows_services()
    assert isinstance(result, dict)


def test_get_raid_controllers(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/raid-controllers",
        json={"results": [], "cursor": None},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_raid_controllers()
    assert isinstance(result, dict)


def test_get_software(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/queries/software",
        json={"results": [{"deviceId": 101, "name": "7-Zip"}], "cursor": None},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_software()
    assert isinstance(result, dict)
