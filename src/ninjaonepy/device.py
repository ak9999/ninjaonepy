from ._http import HttpClient, JsonResponse


class DeviceMixin:
    _http: HttpClient  # injected by Client.__init__

    def get_device(self, device_id: int) -> JsonResponse:
        """Returns details for a specific device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}")

    def get_device_activities(
        self,
        device_id: int,
        older_than: int | None = None,
        newer_than: int | None = None,
        activity_type: str | None = None,
        status: str | None = None,
        series_uid: str | None = None,
        page_size: int | None = None,
        lang: str | None = None,
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns activity log for a device in reverse chronological order.

        Args:
            device_id: Device identifier.
            older_than: Return activities older than this activity ID.
            newer_than: Return activities newer than this activity ID.
            activity_type: Return activities of this type.
            status: Return activities with these statuses.
            series_uid: Return activities related to this alert series.
            page_size: Max number of activities to return.
            lang: Language tag.
            tz: Time zone name.
        """
        return self._http.get(
            f"/v2/device/{device_id}/activities",
            params={
                "olderThan": older_than,
                "newerThan": newer_than,
                "type": activity_type,
                "status": status,
                "seriesUid": series_uid,
                "pageSize": page_size,
                "lang": lang,
                "tz": tz,
            },
        )

    def get_device_disks(self, device_id: int) -> JsonResponse:
        """Returns disk drive details for a device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}/disks")

    def get_device_volumes(self, device_id: int) -> JsonResponse:
        """Returns volume details for a device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}/volumes")

    def get_device_processors(self, device_id: int) -> JsonResponse:
        """Returns processor details for a device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}/processors")

    def get_device_software(self, device_id: int) -> JsonResponse:
        """Returns list of software installed on a device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}/software")

    def get_device_last_logged_on_user(self, device_id: int) -> JsonResponse:
        """Returns the username last logged on to a device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}/last-logged-on-user")

    def get_device_alerts(
        self,
        device_id: int,
        lang: str | None = None,
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns active alerts (triggered conditions) for a device.

        Args:
            device_id: Device identifier.
            lang: Language tag.
            tz: Time zone name.
        """
        return self._http.get(
            f"/v2/device/{device_id}/alerts",
            params={"lang": lang, "tz": tz},
        )

    def get_device_os_patches(
        self,
        device_id: int,
        status: str | None = None,
        patch_type: str | None = None,
        severity: str | None = None,
    ) -> JsonResponse:
        """Returns pending/rejected/approved OS patches for a device.

        Args:
            device_id: Device identifier.
            status: Patch status filter.
            patch_type: Patch type filter.
            severity: Patch severity filter.
        """
        return self._http.get(
            f"/v2/device/{device_id}/os-patches",
            params={"status": status, "type": patch_type, "severity": severity},
        )

    def get_device_installed_os_patches(
        self,
        device_id: int,
        status: str | None = None,
        installed_before: str | None = None,
        installed_after: str | None = None,
    ) -> JsonResponse:
        """Returns OS patch installation history (successful and failed) for a device.

        Args:
            device_id: Device identifier.
            status: Patch status filter (FAILED, INSTALLED).
            installed_before: Include patches installed before this date.
            installed_after: Include patches installed after this date.
        """
        return self._http.get(
            f"/v2/device/{device_id}/os-patch-installs",
            params={
                "status": status,
                "installedBefore": installed_before,
                "installedAfter": installed_after,
            },
        )

    def get_device_software_patches(
        self,
        device_id: int,
        status: str | None = None,
        product_identifier: str | None = None,
        patch_type: str | None = None,
        patch_impact: str | None = None,
    ) -> JsonResponse:
        """Returns pending/rejected third-party software patches for a device.

        Args:
            device_id: Device identifier.
            status: Patch status filter.
            product_identifier: Product identifier filter.
            patch_type: Patch type filter.
            patch_impact: Patch impact filter.
        """
        return self._http.get(
            f"/v2/device/{device_id}/software-patches",
            params={
                "status": status,
                "productIdentifier": product_identifier,
                "type": patch_type,
                "impact": patch_impact,
            },
        )

    def get_device_installed_software_patches(
        self,
        device_id: int,
        status: str | None = None,
        product_identifier: str | None = None,
        patch_type: str | None = None,
        patch_impact: str | None = None,
        installed_before: str | None = None,
        installed_after: str | None = None,
    ) -> JsonResponse:
        """Returns third-party software patch install history for a device.

        Args:
            device_id: Device identifier.
            status: Patch status filter (FAILED, INSTALLED).
            product_identifier: Product identifier filter.
            patch_type: Patch type filter.
            patch_impact: Patch impact filter.
            installed_before: Include patches installed before this date.
            installed_after: Include patches installed after this date.
        """
        return self._http.get(
            f"/v2/device/{device_id}/software-patch-installs",
            params={
                "status": status,
                "productIdentifier": product_identifier,
                "type": patch_type,
                "impact": patch_impact,
                "installedBefore": installed_before,
                "installedAfter": installed_after,
            },
        )

    def get_device_windows_services(
        self,
        device_id: int,
        name: str | None = None,
        state: str | None = None,
    ) -> JsonResponse:
        """Returns Windows services and their statuses for a device.

        Args:
            device_id: Device identifier.
            name: Filter by service name.
            state: Filter by service state. One of: UNKNOWN, STOPPED,
                   START_PENDING, RUNNING, STOP_PENDING, PAUSE_PENDING,
                   PAUSED, CONTINUE_PENDING.
        """
        return self._http.get(
            f"/v2/device/{device_id}/windows-services",
            params={"name": name, "state": state},
        )

    def get_device_active_jobs(
        self,
        device_id: int,
        lang: str | None = None,
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns currently running jobs for a device.

        Args:
            device_id: Device identifier.
            lang: Language tag.
            tz: Time zone name.
        """
        return self._http.get(
            f"/v2/device/{device_id}/jobs",
            params={"lang": lang, "tz": tz},
        )

    def get_device_network_interfaces(self, device_id: int) -> JsonResponse:
        """Returns network interfaces for a device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}/network-interfaces")

    def get_device_maintenance(self, device_id: int) -> JsonResponse:
        """Returns maintenance window status for a device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}/maintenance")
