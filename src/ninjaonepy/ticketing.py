from typing import Any

from ._http import HttpClient, JsonResponse


class TicketingMixin:
    _http: HttpClient  # injected by Client.__init__

    def get_ticket_boards(self) -> JsonResponse:
        """Returns list of ticketing boards."""
        return self._http.get("/v2/ticketing/boards")

    def get_ticket_board(self, board_id: int) -> JsonResponse:
        """Returns details for a specific ticketing board.

        Args:
            board_id: Board identifier.
        """
        return self._http.get(f"/v2/ticketing/board/{board_id}")

    def get_tickets(
        self,
        board_id: int | None = None,
        status: str | None = None,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns list of tickets.

        Args:
            board_id: Filter tickets by board.
            status: Filter by ticket status.
            page_size: Max number of tickets to return.
            after: Last ticket ID from previous page.
        """
        return self._http.get(
            "/v2/ticketing/tickets",
            params={
                "boardId": board_id,
                "status": status,
                "pageSize": page_size,
                "after": after,
            },
        )

    def get_ticket(self, ticket_id: int) -> JsonResponse:
        """Returns details for a specific ticket.

        Args:
            ticket_id: Ticket identifier.
        """
        return self._http.get(f"/v2/ticketing/ticket/{ticket_id}")

    def create_ticket(self, data: dict[str, Any]) -> JsonResponse:
        """Creates a new ticket.

        Args:
            data: Ticket creation payload. At minimum requires ``boardId``,
                  ``subject``, and ``status`` fields.
        """
        return self._http.post("/v2/ticketing/ticket", json=data)

    def update_ticket(self, ticket_id: int, data: dict[str, Any]) -> JsonResponse:
        """Updates an existing ticket.

        Args:
            ticket_id: Ticket identifier.
            data: Fields to update (e.g. status, assignedAppUserId, subject).
        """
        return self._http.patch(f"/v2/ticketing/ticket/{ticket_id}", json=data)

    def delete_ticket(self, ticket_id: int) -> None:
        """Deletes a ticket.

        Args:
            ticket_id: Ticket identifier.
        """
        self._http.delete(f"/v2/ticketing/ticket/{ticket_id}")

    def get_ticket_log_entries(
        self,
        ticket_id: int,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns activity log entries for a ticket.

        Args:
            ticket_id: Ticket identifier.
            page_size: Max number of entries to return.
            after: Last entry ID from previous page.
        """
        return self._http.get(
            f"/v2/ticketing/ticket/{ticket_id}/log-entry",
            params={"pageSize": page_size, "after": after},
        )

    def create_ticket_comment(
        self,
        ticket_id: int,
        comment: str,
        public: bool = True,
    ) -> JsonResponse:
        """Adds a comment to a ticket.

        Args:
            ticket_id: Ticket identifier.
            comment: Comment text (HTML supported).
            public: Whether the comment is visible to the contact. Default True.
        """
        return self._http.post(
            f"/v2/ticketing/ticket/{ticket_id}/log-entry",
            json={"comment": {"body": comment, "public": public}},
        )

    def get_contact_tickets(
        self,
        contact_id: int,
        page_size: int | None = None,
        after: int | None = None,
    ) -> JsonResponse:
        """Returns tickets associated with a contact.

        Args:
            contact_id: Contact identifier.
            page_size: Max number of tickets to return.
            after: Last ticket ID from previous page.
        """
        return self._http.get(
            f"/v2/ticketing/contact/{contact_id}/tickets",
            params={"pageSize": page_size, "after": after},
        )

    def get_ticket_status_list(self) -> JsonResponse:
        """Returns available ticket statuses."""
        return self._http.get("/v2/ticketing/statuses")

    def get_ticket_forms(self) -> JsonResponse:
        """Returns available ticket forms."""
        return self._http.get("/v2/ticketing/trigger-types")
