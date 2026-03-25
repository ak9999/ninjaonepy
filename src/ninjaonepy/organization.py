from typing import Any

from ._http import HttpClient, JsonResponse


class OrganizationMixin:
    _http: HttpClient  # injected by Client.__init__

    def get_organization(self, org_id: int) -> JsonResponse:
        """Returns organization details including policy mapping and locations.

        Args:
            org_id: Organization identifier.
        """
        return self._http.get(f"/v2/organization/{org_id}")

    def get_organization_devices(
        self,
        org_id: int,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of devices for an organization.

        Args:
            org_id: Organization identifier.
            page_size: Max number of devices to return.
            after: Last device ID from previous page.
        """
        return self._http.get(
            f"/v2/organization/{org_id}/devices",
            params={"pageSize": page_size, "after": after},
        )

    def get_organization_locations(self, org_id: int) -> JsonResponse:
        """Returns list of locations for an organization.

        Args:
            org_id: Organization identifier.
        """
        return self._http.get(f"/v2/organization/{org_id}/locations")

    def get_organization_end_users(self, org_id: int) -> JsonResponse:
        """Returns list of end-users for an organization.

        Args:
            org_id: Organization identifier.
        """
        return self._http.get(f"/v2/organization/{org_id}/end-users")

    def create_organization(self, data: dict[str, Any]) -> JsonResponse:
        """Creates a new organization.

        Args:
            data: Organization creation payload. See NinjaOne API docs for
                  required and optional fields.
        """
        return self._http.post("/v2/organizations", json=data)

    def update_organization(self, org_id: int, data: dict[str, Any]) -> JsonResponse:
        """Updates an existing organization.

        Args:
            org_id: Organization identifier.
            data: Fields to update.
        """
        return self._http.patch(f"/v2/organization/{org_id}", json=data)

    def get_organization_custom_fields(self, org_id: int) -> JsonResponse:
        """Returns custom field values for an organization.

        Args:
            org_id: Organization identifier.
        """
        return self._http.get(f"/v2/organization/{org_id}/custom-fields")

    def update_organization_custom_fields(
        self,
        org_id: int,
        fields: dict[str, Any],
    ) -> JsonResponse:
        """Updates custom field values for an organization.

        Args:
            org_id: Organization identifier.
            fields: Mapping of field names to new values.
        """
        return self._http.patch(f"/v2/organization/{org_id}/custom-fields", json=fields)

    def get_organization_location(self, org_id: int, location_id: int) -> JsonResponse:
        """Returns details for a specific location within an organization.

        Args:
            org_id: Organization identifier.
            location_id: Location identifier.
        """
        return self._http.get(f"/v2/organization/{org_id}/location/{location_id}")

    def create_organization_location(
        self,
        org_id: int,
        data: dict[str, Any],
    ) -> JsonResponse:
        """Creates a new location within an organization.

        Args:
            org_id: Organization identifier.
            data: Location creation payload.
        """
        return self._http.post(f"/v2/organization/{org_id}/locations", json=data)

    def update_organization_location(
        self,
        org_id: int,
        location_id: int,
        data: dict[str, Any],
    ) -> JsonResponse:
        """Updates a location within an organization.

        Args:
            org_id: Organization identifier.
            location_id: Location identifier.
            data: Fields to update.
        """
        return self._http.patch(
            f"/v2/organization/{org_id}/location/{location_id}",
            json=data,
        )

    def get_organization_location_custom_fields(
        self,
        org_id: int,
        location_id: int,
    ) -> JsonResponse:
        """Returns custom field values for a location.

        Args:
            org_id: Organization identifier.
            location_id: Location identifier.
        """
        return self._http.get(f"/v2/organization/{org_id}/location/{location_id}/custom-fields")

    def update_organization_location_custom_fields(
        self,
        org_id: int,
        location_id: int,
        fields: dict[str, Any],
    ) -> JsonResponse:
        """Updates custom field values for a location.

        Args:
            org_id: Organization identifier.
            location_id: Location identifier.
            fields: Mapping of field names to new values.
        """
        return self._http.patch(
            f"/v2/organization/{org_id}/location/{location_id}/custom-fields",
            json=fields,
        )

    def get_contacts(
        self,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of all contacts across all organizations.

        Args:
            page_size: Max number of contacts to return.
            after: Last contact ID from previous page.
        """
        return self._http.get(
            "/v2/contacts",
            params={"pageSize": page_size, "after": after},
        )

    def get_contact(self, contact_id: int) -> JsonResponse:
        """Returns details for a specific contact.

        Args:
            contact_id: Contact identifier.
        """
        return self._http.get(f"/v2/contact/{contact_id}")

    def create_contact(self, data: dict[str, Any]) -> JsonResponse:
        """Creates a new contact.

        Args:
            data: Contact creation payload.
        """
        return self._http.post("/v2/contacts", json=data)

    def update_contact(self, contact_id: int, data: dict[str, Any]) -> JsonResponse:
        """Updates an existing contact.

        Args:
            contact_id: Contact identifier.
            data: Fields to update.
        """
        return self._http.patch(f"/v2/contact/{contact_id}", json=data)

    def delete_contact(self, contact_id: int) -> None:
        """Deletes a contact.

        Args:
            contact_id: Contact identifier.
        """
        self._http.delete(f"/v2/contact/{contact_id}")

    def get_organization_alerts(
        self,
        org_id: int,
        lang: str | None = None,
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns active alerts for an organization.

        Args:
            org_id: Organization identifier.
            lang: Language tag.
            tz: Time zone name.
        """
        return self._http.get(
            f"/v2/organization/{org_id}/alerts",
            params={"lang": lang, "tz": tz},
        )

    def get_organization_jobs(
        self,
        org_id: int,
        lang: str | None = None,
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns running jobs for an organization.

        Args:
            org_id: Organization identifier.
            lang: Language tag.
            tz: Time zone name.
        """
        return self._http.get(
            f"/v2/organization/{org_id}/jobs",
            params={"lang": lang, "tz": tz},
        )

    def get_organization_activities(
        self,
        org_id: int,
        older_than: int | None = None,
        newer_than: int | None = None,
        activity_type: str | None = None,
        status: str | None = None,
        page_size: int | None = None,
        lang: str | None = None,
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns activity log for an organization.

        Args:
            org_id: Organization identifier.
            older_than: Return activities older than this activity ID.
            newer_than: Return activities newer than this activity ID.
            activity_type: Return activities of this type.
            status: Return activities with these statuses.
            page_size: Max number of activities to return.
            lang: Language tag.
            tz: Time zone name.
        """
        return self._http.get(
            f"/v2/organization/{org_id}/activities",
            params={
                "olderThan": older_than,
                "newerThan": newer_than,
                "type": activity_type,
                "status": status,
                "pageSize": page_size,
                "lang": lang,
                "tz": tz,
            },
        )
