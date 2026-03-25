from ._http import HttpClient, JsonResponse


class BackupMixin:
    _http: HttpClient  # injected by Client.__init__

    def get_backup_jobs(
        self,
        df: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns backup job status records across devices.

        Args:
            df: Device filter string.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/backup/jobs",
            params={"df": df, "cursor": cursor, "pageSize": page_size},
        )

    def get_backup_usage(
        self,
        df: str | None = None,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns backup storage usage across devices.

        Args:
            df: Device filter string.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            "/v2/backup/usages",
            params={"df": df, "cursor": cursor, "pageSize": page_size},
        )

    def get_device_backup_jobs(
        self,
        device_id: int,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns backup job history for a specific device.

        Args:
            device_id: Device identifier.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            f"/v2/device/{device_id}/backup/jobs",
            params={"cursor": cursor, "pageSize": page_size},
        )

    def get_device_backup_usage(self, device_id: int) -> JsonResponse:
        """Returns backup storage usage for a specific device.

        Args:
            device_id: Device identifier.
        """
        return self._http.get(f"/v2/device/{device_id}/backup/usage")

    def get_organization_backup_jobs(
        self,
        org_id: int,
        cursor: str | None = None,
        page_size: int | None = None,
    ) -> JsonResponse:
        """Returns backup job history for all devices in an organization.

        Args:
            org_id: Organization identifier.
            cursor: Pagination cursor name.
            page_size: Max number of records to return.
        """
        return self._http.get(
            f"/v2/organization/{org_id}/backup/jobs",
            params={"cursor": cursor, "pageSize": page_size},
        )

    def get_organization_backup_usage(self, org_id: int) -> JsonResponse:
        """Returns backup storage usage for an organization.

        Args:
            org_id: Organization identifier.
        """
        return self._http.get(f"/v2/organization/{org_id}/backup/usage")
