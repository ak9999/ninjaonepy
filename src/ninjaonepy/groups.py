from ._http import HttpClient, JsonResponse


class GroupsMixin:
    _http: HttpClient  # injected by Client.__init__

    def get_group_device_ids(
        self,
        group_id: int,
        refresh: bool | None = None,
    ) -> JsonResponse:
        """Returns device IDs that match the group (saved search) criteria.

        Args:
            group_id: Group identifier.
            refresh: Re-evaluate the group criteria before returning results.
        """
        return self._http.get(
            f"/v2/group/{group_id}/device-ids",
            params={"refresh": refresh},
        )
