# integrations/

API client wrappers for external systems. Keeps third-party API calls in one place
instead of scattered through the codebase.

- **`netbox.py`** — Pull inventory/device data, push config backups and state.
- **`servicenow.py`** — Create tickets on compliance failures or change events.
- **`monitoring.py`** — Push alerts / register devices with monitoring.

Each client reads its credentials from `config/` (environment-backed), never inline.
