# Local HTTP Server — Status Check Endpoint

A lightweight, standalone HTTP server built using **only Python's standard library** (`http.server`, `json`). No third-party frameworks (Flask, FastAPI, Django) are used.

## Objective

Expose a simple system status check endpoint over HTTP, demonstrating manual request routing and JSON response handling using `BaseHTTPRequestHandler`.

## Technical Specifications

| Spec | Value |
|---|---|
| Language | Python 3 (standard library only) |
| Target file | `server.py` |
| Host | `localhost` |
| Port | `8080` |

## Getting Started

### Prerequisites

- Python 3.x installed (no external packages required)

### Run the server

```bash
python server.py
```

You should see:

```
Serving on http://localhost:8080
```

Press `Ctrl+C` to stop the server — it shuts down gracefully without printing a traceback.

##  API Endpoints

### `GET /status`

Returns the current server status.

**Request:**
```bash
curl -i http://localhost:8080/status
```

**Response:** `200 OK`
```json
{
  "status": "running",
  "code": 200,
  "message": "Server is operational"
}
```

### Any other route or method

Any unmapped route, or any HTTP method other than `GET /status` (POST, PUT, PATCH, DELETE, OPTIONS, etc.), returns a `404`.

**Request:**
```bash
curl -i http://localhost:8080/other
```

**Response:** `404 Not Found`
```json
{
  "error": "Endpoint not found"
}
```

## Testing

```bash
# Test 1: Valid status request
curl -i http://localhost:8080/status

# Test 2: Invalid route
curl -i http://localhost:8080/other

# Test 3: Unsupported method
curl -i  http://localhost:8080/status -X POST
```

## Implementation Notes

- Built on `BaseHTTPRequestHandler` from Python's built-in `http.server` module.
- `_send_json()` centralizes response building (status code, `Content-Type: application/json` header, JSON body).
- `__getattr__` is overridden so that **any** unimplemented HTTP method (`do_POST`, `do_PATCH`, `do_HEAD`, etc.) automatically falls back to the 404 handler, instead of requiring one method per verb.
- `server.server_close()` is called on shutdown to release the socket cleanly after `Ctrl+C`.

