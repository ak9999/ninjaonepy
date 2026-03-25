class NinjaError(Exception):
    """Base exception for all ninjaonepy errors."""


class AuthError(NinjaError):
    """Raised on 401/403 responses."""


class NotFoundError(NinjaError):
    """Raised on 404 responses."""


class RateLimitError(NinjaError):
    """Raised on 429 responses."""
