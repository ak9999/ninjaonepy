# NinjaOne API Python Client

A clean, slim, synchronous Python 3.12+ client for the [NinjaOne RMM API v2](https://app.ninjaone.com/apidocs/).

## Features

- **Minimal dependencies**: Uses only `httpx` for HTTP.
- **OAuth2 authentication**: Client Credentials flow (server-to-server). Tokens are cached and automatically refreshed.
- **Clean API**: snake_case method names and raw dict/list responses. No bloated wrapper objects.
- **Type-safe**: Full type hints and mypy strict mode support.

## Requirements

- Python 3.12 or higher
- `httpx >= 0.27`

## Installation

Install from the repository:

```bash
pip install git+https://github.com/ak9999/ninjaonepy.git
```

## Quick Start

```python
from ninjaonepy import Client

# Create a client using OAuth2 credentials
with Client(
    client_id="your_client_id",
    client_secret="your_client_secret",
    europe=False,  # Use True for EU data centre
) as client:
    # Get all organizations
    orgs = client.get_organizations()
    print(orgs)

    # Get devices
    devices = client.get_devices()
    print(devices)
```

### Using Environment Variables

```python
import os
from ninjaonepy import Client

client_id = os.environ.get("NINJA_CLIENT_ID")
client_secret = os.environ.get("NINJA_CLIENT_SECRET")

if not client_id or not client_secret:
    raise ValueError("NINJA_CLIENT_ID and NINJA_CLIENT_SECRET are required")

with Client(client_id=client_id, client_secret=client_secret) as client:
    orgs = client.get_organizations()
```

## API Overview

The client is organized into logical mixins:

### System
- `get_organizations()` — List all organizations
- `get_devices()` — List all devices with basic info
- `get_devices_detailed()` — List devices with full details
- `get_antivirus_status()` — Get AV status for all devices
- `get_antivirus_threats()` — Get detected threats
- And more...

### Organization
- `get_organization(id)` — Get a specific organization
- `create_organization(data)` — Create an organization
- `update_organization(id, data)` — Update an organization
- And more...

### Device
- `get_device(id)` — Get a specific device
- `get_device_details(id)` — Get full device details
- And more...

### Management
- `reset_alert(...)` — Reset an alert
- `approve_alert(...)` — Approve an alert
- And more...

### Queries
- `query_devices(...)` — Run a bulk device query
- And more...

### Groups, Ticketing, Backup, Custom Fields, Vulnerability Management
- See the source code and API documentation for complete endpoint lists.

## Responses

All API methods return raw dictionaries or lists—no wrapper objects. For example:

```python
orgs = client.get_organizations()
# orgs is a list of dicts:
# [
#   {"id": 1, "name": "Acme Corp", "description": "..."},
#   {"id": 2, "name": "Globex", "description": "..."},
# ]
```

## Error Handling

The client raises typed exceptions for common errors:

```python
from ninjaonepy._exceptions import AuthError, NotFoundError, RateLimitError, NinjaError

try:
    with Client(client_id="bad", client_secret="creds") as client:
        client.get_organizations()
except AuthError:
    print("Invalid credentials")
except NotFoundError:
    print("Resource not found")
except RateLimitError:
    print("Rate limited; try again later")
except NinjaError as e:
    print(f"API error: {e}")
```

## Development

### Setup

```bash
uv sync --group dev
```

### Run Tests

```bash
uv run pytest
```

### Lint & Format

```bash
uv run ruff check src tests
uv run ruff format src tests
```

### Type Check

```bash
uv run mypy src
```

### Build

```bash
uv build
```

## Authentication

The client uses **OAuth2 Client Credentials** flow:

1. You provide `client_id` and `client_secret` from the NinjaOne admin portal.
2. The client automatically fetches a Bearer token on first use.
3. Tokens are cached and refreshed 30 seconds before expiry.
4. Tokens are requested from:
   - US: `https://app.ninjarmm.com/oauth/token`
   - EU: `https://eu.ninjarmm.com/oauth/token`

## Migration from ninjarmmpy v0.2

The old `ninjarmmpy` package used HMAC-SHA1 signing, which is no longer supported by NinjaOne. This rewrite uses OAuth2.

### Breaking Changes

| Old API               | New API              |
|----------------------|----------------------|
| `ninjarmmpy`         | `ninjaonepy`         |
| `AccessKeyID`        | `client_id`          |
| `SecretAccessKey`    | `client_secret`      |
| `getOrganizations()` | `get_organizations()`|
| `Europe=False`       | `europe=False`       |

The old code will not work without updating credentials and method names.

## License

MIT — See [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please ensure all tests pass and code is linted with ruff and type-checked with mypy before submitting a PR.

## References

- [NinjaOne API v2 Documentation](https://app.ninjaone.com/apidocs/)
- [NinjaOne Support](https://support.ninjaone.com/)
