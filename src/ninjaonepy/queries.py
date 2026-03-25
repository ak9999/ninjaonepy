from ._http import HttpClient, JsonResponse


class QueriesMixin:
    _http: HttpClient  # injected by Client.__init__

    def get_antivirus_threats(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns list of antivirus threats detected across devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/antivirus-threats",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_antivirus_status(
        self,
        df: str | None = None,
        ts: str | None = None,
        product_state: str | None = None,
        product_name: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns antivirus software status for devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            product_state: Product state filter.
            product_name: Product name filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/antivirus-status",
            params={
                "df": df,
                "ts": ts,
                "productState": product_state,
                "productName": product_name,
                "cursor": cursor,
                "pageSize": page_size,
            },
        )

    def get_operating_systems(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns operating system information for devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/operating-systems",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_processors(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns processor information for devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/processors",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_volumes(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns disk volume information for devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/volumes",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_disk_drives(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns physical disk information for devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/disks",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_computer_systems(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns computer system (BIOS, chassis, etc.) information for devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/computer-systems",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_device_health(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns device health summary records.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/device-health",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_software(
        self,
        df: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
        installed_before: str | None = None,
        installed_after: str | None = None,
    ) -> JsonResponse:
        """Returns installed software across devices.

        Args:
            df: Device filter string.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
            installed_before: Include software installed before this date.
            installed_after: Include software installed after this date.
        """
        return self._http.get(
            "/v2/queries/software",
            params={
                "df": df,
                "cursor": cursor,
                "pageSize": page_size,
                "installedBefore": installed_before,
                "installedAfter": installed_after,
            },
        )

    def get_os_patches(
        self,
        df: str | None = None,
        ts: str | None = None,
        status: str | None = None,
        patch_type: str | None = None,
        severity: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns OS patches for which there were no installation attempts.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            status: Patch status filter.
            patch_type: Patch type filter.
            severity: Patch severity filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/os-patches",
            params={
                "df": df,
                "ts": ts,
                "status": status,
                "type": patch_type,
                "severity": severity,
                "cursor": cursor,
                "pageSize": page_size,
            },
        )

    def get_installed_os_patches(
        self,
        df: str | None = None,
        status: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
        installed_before: str | None = None,
        installed_after: str | None = None,
    ) -> JsonResponse:
        """Returns OS patch installation history (successful and failed).

        Args:
            df: Device filter string.
            status: Patch status filter (FAILED, INSTALLED).
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
            installed_before: Include patches installed before this date.
            installed_after: Include patches installed after this date.
        """
        return self._http.get(
            "/v2/queries/os-patch-installs",
            params={
                "df": df,
                "status": status,
                "cursor": cursor,
                "pageSize": page_size,
                "installedBefore": installed_before,
                "installedAfter": installed_after,
            },
        )

    def get_software_patches(
        self,
        df: str | None = None,
        ts: str | None = None,
        status: str | None = None,
        product_identifier: str | None = None,
        patch_type: str | None = None,
        impact: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns third-party software patches with no installation attempts.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            status: Patch status filter.
            product_identifier: Product identifier filter.
            patch_type: Patch type filter.
            impact: Patch impact filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/software-patches",
            params={
                "df": df,
                "ts": ts,
                "status": status,
                "productIdentifier": product_identifier,
                "type": patch_type,
                "impact": impact,
                "cursor": cursor,
                "pageSize": page_size,
            },
        )

    def get_installed_software_patches(
        self,
        df: str | None = None,
        ts: str | None = None,
        status: str | None = None,
        product_identifier: str | None = None,
        patch_type: str | None = None,
        impact: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
        installed_before: str | None = None,
        installed_after: str | None = None,
    ) -> JsonResponse:
        """Returns third-party software patch installation history.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            status: Patch status filter.
            product_identifier: Product identifier filter.
            patch_type: Patch type filter.
            impact: Patch impact filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
            installed_before: Include patches installed before this date.
            installed_after: Include patches installed after this date.
        """
        return self._http.get(
            "/v2/queries/software-patch-installs",
            params={
                "df": df,
                "ts": ts,
                "status": status,
                "productIdentifier": product_identifier,
                "type": patch_type,
                "impact": impact,
                "cursor": cursor,
                "pageSize": page_size,
                "installedBefore": installed_before,
                "installedAfter": installed_after,
            },
        )

    def get_raid_controllers(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns RAID controller information for devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/raid-controllers",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_raid_drives(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns drives connected to RAID controllers across devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/raid-drives",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_windows_services(
        self,
        df: str | None = None,
        name: str | None = None,
        state: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns Windows service status across devices.

        Args:
            df: Device filter string.
            name: Service name filter.
            state: Service state filter. One of: UNKNOWN, STOPPED,
                   START_PENDING, RUNNING, STOP_PENDING, PAUSE_PENDING,
                   PAUSED, CONTINUE_PENDING.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/windows-services",
            params={
                "df": df,
                "name": name,
                "state": state,
                "cursor": cursor,
                "pageSize": page_size,
            },
        )

    def get_last_logged_on_users(
        self,
        df: str | None = None,
        cursor: str | None = None,
        page_size: int = 1000,
    ) -> JsonResponse:
        """Returns usernames and logon times across devices.

        Args:
            df: Device filter string.
            cursor: Pagination cursor name.
            page_size: Max number of records to return. Defaults to 1000.
        """
        return self._http.get(
            "/v2/queries/logged-on-users",
            params={"df": df, "cursor": cursor, "pageSize": page_size},
        )

    def get_network_interfaces(
        self,
        df: str | None = None,
        ts: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns network interface information across devices.

        Args:
            df: Device filter string.
            ts: Monitoring timestamp filter.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/queries/network-interfaces",
            params={"df": df, "ts": ts, "cursor": cursor, "pageSize": page_size},
        )

    def get_custom_fields(
        self,
        df: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
        updated_after: str | None = None,
    ) -> JsonResponse:
        """Returns custom field values across devices.

        Args:
            df: Device filter string.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
            updated_after: Include records updated after this date.
        """
        return self._http.get(
            "/v2/queries/custom-fields",
            params={
                "df": df,
                "cursor": cursor,
                "pageSize": page_size,
                "updatedAfter": updated_after,
            },
        )

    def get_scripting_options(
        self,
        df: str | None = None,
        lang: str | None = None,
    ) -> JsonResponse:
        """Returns available scripting options across devices.

        Args:
            df: Device filter string.
            lang: Language tag.
        """
        return self._http.get(
            "/v2/queries/scripting/options",
            params={"df": df, "lang": lang},
        )
