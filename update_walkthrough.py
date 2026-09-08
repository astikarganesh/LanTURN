import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\walkthrough.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

walkthrough_update = """
## QA Hardening Phase

### 1. Lifecycle and Memory Resilience
- Audited all UI screens and replaced standard `collectAsState()` with `collectAsStateWithLifecycle()`. This ensures flows pause properly when the app is backgrounded, mitigating memory leaks and unnecessary network calls.

### 2. Network & Global Session Management
- Discovered that expired tokens caused localized failures.
- **Implemented Global `AuthEventBus`**: Created a centralized event flow. When `TokenAuthenticator` detects a 401 Unauthorized from any API call, it emits `AuthEvent.Unauthorized`.
- The root `AppNavigation` compositor now listens to `AuthEventBus` and automatically purges the session and redirects to the Login screen upon failure.

### 3. Background Notifications Simulation
- The backend doesn't support FCM token integration.
- **Implemented WorkManager**: Added `androidx.work:work-runtime-ktx` and `io.insert-koin:koin-androidx-workmanager`.
- Created a `NotificationWorker` that wakes up periodically (every 15 minutes) when connected to a network to poll `/api/notifications/unread`.
- If new notifications are detected, it triggers local Android notifications using `NotificationManagerCompat`.

### 4. UI Edge Cases (Rotation Resilience)
- **State Preservation**: Text input fields (Login, Registration, Profile Editing, Job Creation) previously lost state on screen rotation because they used standard `remember`.
- Replaced all inputs with `rememberSaveable` to protect against configuration changes.
"""

content += walkthrough_update

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)