from typing import Any

from ._http import HttpClient, JsonResponse


class ManagementMixin:
    _http: HttpClient  # injected by Client.__init__

    def reset_alert(self, uid: str) -> None:
        """Resets (dismisses) an alert/triggered condition by UID.

        Args:
            uid: Unique identifier of the alert/condition.
        """
        self._http.delete(f"/v2/alert/{uid}")

    def approve_devices(self, device_ids: list[int]) -> JsonResponse:
        """Approves devices that are waiting for approval.

        Args:
            device_ids: List of device identifiers to approve.
        """
        return self._http.post(
            "/v2/devices/approval/APPROVE",
            json={"devices": device_ids},
        )

    def reject_devices(self, device_ids: list[int]) -> JsonResponse:
        """Rejects devices that are waiting for approval.

        Args:
            device_ids: List of device identifiers to reject.
        """
        return self._http.post(
            "/v2/devices/approval/REJECT",
            json={"devices": device_ids},
        )

    def run_device_script(
        self,
        device_id: int,
        script_id: int,
        run_as: str | None = None,
        parameters: str | None = None,
    ) -> JsonResponse:
        """Runs a script on a device.

        Args:
            device_id: Device identifier.
            script_id: Script identifier.
            run_as: Credential identifier to run the script as.
            parameters: Script parameters.
        """
        body: dict[str, Any] = {"id": script_id}
        if run_as is not None:
            body["runAs"] = run_as
        if parameters is not None:
            body["parameters"] = parameters
        return self._http.post(f"/v2/device/{device_id}/script/run", json=body)

    def reboot_device(
        self,
        device_id: int,
        mode: str = "NORMAL",
        reason: str | None = None,
    ) -> JsonResponse:
        """Queues a reboot for a device.

        Args:
            device_id: Device identifier.
            mode: Reboot mode. One of: NORMAL, FORCED. Defaults to NORMAL.
            reason: Optional reason for the reboot.
        """
        body: dict[str, Any] = {"mode": mode}
        if reason is not None:
            body["reason"] = reason
        return self._http.post(f"/v2/device/{device_id}/reboot/{mode}", json=body)

    def update_device(self, device_id: int, data: dict[str, Any]) -> JsonResponse:
        """Updates device attributes (display name, node role, policy, etc.).

        Args:
            device_id: Device identifier.
            data: Fields to update.
        """
        return self._http.patch(f"/v2/device/{device_id}", json=data)

    def set_device_maintenance(
        self,
        device_id: int,
        enabled: bool,
        duration_minutes: int | None = None,
    ) -> JsonResponse:
        """Enables or disables maintenance mode for a device.

        Args:
            device_id: Device identifier.
            enabled: True to enable maintenance mode, False to disable.
            duration_minutes: Duration in minutes before maintenance mode ends
                              automatically (only applicable when enabling).
        """
        body: dict[str, Any] = {"enabled": enabled}
        if duration_minutes is not None:
            body["durationMinutes"] = duration_minutes
        return self._http.post(f"/v2/device/{device_id}/maintenance", json=body)

    def delete_device(self, device_id: int) -> None:
        """Deletes/removes a device.

        Args:
            device_id: Device identifier.
        """
        self._http.delete(f"/v2/device/{device_id}")

    def get_webhooks(self) -> JsonResponse:
        """Returns list of configured webhooks."""
        return self._http.get("/v2/webhook")

    def create_webhook(self, data: dict[str, Any]) -> JsonResponse:
        """Creates a new webhook.

        Args:
            data: Webhook creation payload. Requires at minimum ``url`` and
                  ``activityType`` fields.
        """
        return self._http.post("/v2/webhook", json=data)

    def update_webhook(self, webhook_id: int, data: dict[str, Any]) -> JsonResponse:
        """Updates an existing webhook.

        Args:
            webhook_id: Webhook identifier.
            data: Fields to update.
        """
        return self._http.patch(f"/v2/webhook/{webhook_id}", json=data)

    def delete_webhook(self, webhook_id: int) -> None:
        """Deletes a webhook.

        Args:
            webhook_id: Webhook identifier.
        """
        self._http.delete(f"/v2/webhook/{webhook_id}")

    def install_os_patches(
        self,
        device_id: int,
        patch_ids: list[int] | None = None,
        reboot: str = "AS_NEEDED",
    ) -> JsonResponse:
        """Triggers OS patch installation on a device.

        Args:
            device_id: Device identifier.
            patch_ids: List of specific OS patch IDs to install.
                       If omitted, all approved pending patches are installed.
            reboot: Reboot behaviour after patching. One of: AS_NEEDED,
                    ALWAYS, NEVER. Defaults to AS_NEEDED.
        """
        body: dict[str, Any] = {"reboot": reboot}
        if patch_ids is not None:
            body["patches"] = patch_ids
        return self._http.post(
            f"/v2/device/{device_id}/patch-management/patches/install", json=body
        )

    def install_software_patches(
        self,
        device_id: int,
        patch_ids: list[int] | None = None,
        reboot: str = "AS_NEEDED",
    ) -> JsonResponse:
        """Triggers third-party software patch installation on a device.

        Args:
            device_id: Device identifier.
            patch_ids: List of specific software patch IDs to install.
                       If omitted, all approved pending patches are installed.
            reboot: Reboot behaviour after patching. One of: AS_NEEDED,
                    ALWAYS, NEVER. Defaults to AS_NEEDED.
        """
        body: dict[str, Any] = {"reboot": reboot}
        if patch_ids is not None:
            body["patches"] = patch_ids
        return self._http.post(
            f"/v2/device/{device_id}/patch-management/software-patches/install",
            json=body,
        )

    def send_device_notification(
        self,
        device_id: int,
        title: str,
        message: str,
    ) -> JsonResponse:
        """Sends a notification/message to a device.

        Args:
            device_id: Device identifier.
            title: Notification title.
            message: Notification body text.
        """
        return self._http.post(
            f"/v2/device/{device_id}/message",
            json={"title": title, "body": message},
        )
