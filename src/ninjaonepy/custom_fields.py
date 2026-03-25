from typing import Any

from ._http import HttpClient, JsonResponse


class CustomFieldsMixin:
    _http: HttpClient  # injected by Client.__init__

    def get_device_custom_fields(
        self,
        device_id: int,
        fields: str | None = None,
    ) -> JsonResponse:
        """Returns custom field values for a device.

        Args:
            device_id: Device identifier.
            fields: Comma-separated list of specific field names to return.
        """
        return self._http.get(
            f"/v2/device/{device_id}/custom-fields",
            params={"fields": fields},
        )

    def update_device_custom_fields(
        self,
        device_id: int,
        fields: dict[str, Any],
    ) -> JsonResponse:
        """Updates custom field values for a device.

        Args:
            device_id: Device identifier.
            fields: Mapping of custom field names to their new values.
        """
        return self._http.patch(f"/v2/device/{device_id}/custom-fields", json=fields)

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
            fields: Mapping of custom field names to their new values.
        """
        return self._http.patch(f"/v2/organization/{org_id}/custom-fields", json=fields)

    def get_location_custom_fields(
        self,
        org_id: int,
        location_id: int,
    ) -> JsonResponse:
        """Returns custom field values for an organization location.

        Args:
            org_id: Organization identifier.
            location_id: Location identifier.
        """
        return self._http.get(f"/v2/organization/{org_id}/location/{location_id}/custom-fields")

    def update_location_custom_fields(
        self,
        org_id: int,
        location_id: int,
        fields: dict[str, Any],
    ) -> JsonResponse:
        """Updates custom field values for an organization location.

        Args:
            org_id: Organization identifier.
            location_id: Location identifier.
            fields: Mapping of custom field names to their new values.
        """
        return self._http.patch(
            f"/v2/organization/{org_id}/location/{location_id}/custom-fields",
            json=fields,
        )

    def get_custom_field_definitions(
        self,
        scope: str | None = None,
    ) -> JsonResponse:
        """Returns defined custom fields (their names, types, and scopes).

        Args:
            scope: Filter by scope. One of: NODE, ORGANIZATION, LOCATION.
        """
        return self._http.get(
            "/v2/custom-fields",
            params={"scope": scope},
        )
