from ._http import HttpClient, JsonResponse


class SystemMixin:
    _http: HttpClient  # injected by Client.__init__

    def get_organizations(
        self,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of organizations (brief mode).

        Args:
            page_size: Max number of organizations to return.
            after: Last organization ID from previous page (pagination cursor).
        """
        return self._http.get(
            "/v2/organizations",
            params={"pageSize": page_size, "after": after},
        )

    def get_organizations_detailed(
        self,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of organizations with locations and policy mappings.

        Args:
            page_size: Max number of organizations to return.
            after: Last organization ID from previous page (pagination cursor).
        """
        return self._http.get(
            "/v2/organizations-detailed",
            params={"pageSize": page_size, "after": after},
        )

    def get_devices(
        self,
        df: str | None = None,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of devices (basic node information).

        Args:
            df: Device filter string. See NinjaOne Device Filter Syntax docs.
            page_size: Max number of devices to return.
            after: Last node ID from previous page.
        """
        return self._http.get(
            "/v2/devices",
            params={"df": df, "pageSize": page_size, "after": after},
        )

    def get_devices_detailed(
        self,
        df: str | None = None,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of devices with additional information.

        Args:
            df: Device filter string. See NinjaOne Device Filter Syntax docs.
            page_size: Max number of devices to return.
            after: Last node ID from previous page.
        """
        return self._http.get(
            "/v2/devices-detailed",
            params={"df": df, "pageSize": page_size, "after": after},
        )

    def get_alerts(
        self,
        source_type: str | None = None,
        df: str | None = None,
        lang: str | None = None,
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns list of active alerts/triggered conditions.

        Args:
            source_type: Source of the alert/triggered condition.
            df: Device filter string.
            lang: Language tag (e.g. "en").
            tz: Time zone name.
        """
        return self._http.get(
            "/v2/alerts",
            params={"sourceType": source_type, "df": df, "lang": lang, "tz": tz},
        )

    def get_active_jobs(
        self,
        job_type: str | None = None,
        df: str | None = None,
        lang: str | None = None,
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns list of running jobs.

        Args:
            job_type: Job type filter.
            df: Device filter string.
            lang: Language tag.
            tz: Time zone name.
        """
        return self._http.get(
            "/v2/jobs",
            params={"jobType": job_type, "df": df, "lang": lang, "tz": tz},
        )

    def get_activities(
        self,
        activity_class: str = "ALL",
        before: str | None = None,
        after: str | None = None,
        older_than: int | None = None,
        newer_than: int | None = None,
        activity_type: str | None = None,
        status: str | None = None,
        user: str | None = None,
        series_uid: str | None = None,
        df: str | None = None,
        page_size: int = 200,
        lang: str = "en",
        tz: str | None = None,
    ) -> JsonResponse:
        """Returns activity log in reverse chronological order.

        Args:
            activity_class: Filter by class. One of: ALL, SYSTEM, DEVICE.
            before: Return activities recorded before this date.
            after: Return activities recorded after this date.
            older_than: Return activities older than this activity ID.
            newer_than: Return activities newer than this activity ID.
            activity_type: Return activities of this type.
            status: Return activities with these statuses.
            user: Return activities for this user.
            series_uid: Return activities related to this alert series.
            df: Device filter string.
            page_size: Max number of activities to return.
            lang: Language tag.
            tz: Time zone name.
        """
        return self._http.get(
            "/v2/activities",
            params={
                "activityClass": activity_class,
                "before": before,
                "after": after,
                "olderThan": older_than,
                "newerThan": newer_than,
                "type": activity_type,
                "status": status,
                "user": user,
                "seriesUid": series_uid,
                "df": df,
                "pageSize": page_size,
                "lang": lang,
                "tz": tz,
            },
        )

    def get_locations(
        self,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of all locations across all organizations.

        Args:
            page_size: Max number of locations to return.
            after: Last location ID from previous page.
        """
        return self._http.get(
            "/v2/locations",
            params={"pageSize": page_size, "after": after},
        )

    def get_node_roles(self) -> JsonResponse:
        """Returns list of device roles."""
        return self._http.get("/v2/roles")

    def get_policies(self) -> JsonResponse:
        """Returns list of policies."""
        return self._http.get("/v2/policies")

    def get_software_products(self) -> JsonResponse:
        """Returns available software products (third-party patching)."""
        return self._http.get("/v2/software-products")

    def get_scheduled_tasks(self) -> JsonResponse:
        """Returns list of registered scheduled tasks."""
        return self._http.get("/v2/tasks")

    def get_users(self, user_type: str | None = None) -> JsonResponse:
        """Returns list of users (technicians and end-users by default).

        Args:
            user_type: Filter by user type. One of: TECHNICIAN, END_USER.
        """
        return self._http.get("/v2/users", params={"userType": user_type})

    def get_groups(self, lang: str | None = None) -> JsonResponse:
        """Returns list of groups (saved searches).

        Args:
            lang: Language tag for group descriptions.
        """
        return self._http.get("/v2/groups", params={"lang": lang})

    def get_attachment(self, attachment_id: str) -> JsonResponse:
        """Returns an attachment (image, document) by ID.

        Args:
            attachment_id: Attachment identifier.
        """
        return self._http.get(f"/v2/attachment/{attachment_id}")

    def get_knowledge_base_articles(
        self,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of knowledge base articles.

        Args:
            page_size: Max number of articles to return.
            after: Last article ID from previous page.
        """
        return self._http.get(
            "/v2/knowledgebase",
            params={"pageSize": page_size, "after": after},
        )

    def get_organization_documents(
        self,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of organization documents.

        Args:
            page_size: Max number of documents to return.
            after: Last document ID from previous page.
        """
        return self._http.get(
            "/v2/organization/documents",
            params={"pageSize": page_size, "after": after},
        )

    def get_asset_tags(self) -> JsonResponse:
        """Returns list of asset tags."""
        return self._http.get("/v2/tags")

    def get_policy(self, policy_id: int) -> JsonResponse:
        """Returns details for a specific policy.

        Args:
            policy_id: Policy identifier.
        """
        return self._http.get(f"/v2/policy/{policy_id}")

    def get_software_patch_cycle(self) -> JsonResponse:
        """Returns configured software patch cycles."""
        return self._http.get("/v2/patch-management/patch-cycle")

    def get_related_items(self, entity_type: str, entity_id: int) -> JsonResponse:
        """Returns items related to the given entity.

        Args:
            entity_type: Type of the entity (e.g. device, organization).
            entity_id: Entity identifier.
        """
        return self._http.get(f"/v2/related-items/with-entity/{entity_type}/{entity_id}")

    def get_dashboard_summary(self) -> JsonResponse:
        """Returns system-wide health and device count summary."""
        return self._http.get("/v2/dashboard/counts")
