from pytest_httpx import HTTPXMock

from ninjaonepy import Client


def test_reset_alert(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/alert/abc-123",
        status_code=204,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        client.reset_alert("abc-123")  # should not raise


def test_approve_devices(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/devices/approval/APPROVE",
        json={"success": True},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.approve_devices([101, 102])
    assert result == {"success": True}


def test_reject_devices(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/devices/approval/REJECT",
        json={"success": True},
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.reject_devices([103])
    assert result == {"success": True}


def test_get_webhooks(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/webhook",
        json=[{"id": 1, "url": "https://example.com/hook"}],
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        result = client.get_webhooks()
    assert isinstance(result, list)


def test_delete_device(auth_mock: HTTPXMock) -> None:
    auth_mock.add_response(
        url="https://app.ninjarmm.com/v2/device/101",
        status_code=204,
    )
    with Client(client_id="test-id", client_secret="test-secret") as client:
        client.delete_device(101)  # should not raise
