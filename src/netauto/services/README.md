# services/

The actual automation logic — the workflows that do real work and need custom logic,
parsing, or error handling that Ansible is clumsy at.

## Example services

- **`backup.py`** — Connect to all devices, pull running config, store it, upload to NetBox.
- **`drift_detection.py`** — Compare running config against `configs/golden/`, flag differences.
- **`compliance_audit.py`** — Verify every device meets policy (NTP, syslog, SNMP, etc.).

Each service uses `core/` for connectivity and `integrations/` for external systems, and
writes output to `reports/`.
