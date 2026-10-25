# Flask Application Context vs Request Context

Flask manages state using two thread-local proxies:

1. **Application Context (`current_app`, `g`)**:
   - Tied to the running Flask application instance.
   - `g`: Temporary storage for global variables during a single request (e.g. database connections, authenticated user context).

2. **Request Context (`request`, `session`)**:
   - Tied to an incoming HTTP request.
   - `request`: Contains query params, form payloads, JSON body, headers, and cookies.
   - `session`: Cryptographically signed cookie storing user identity across requests.
