# src/netauto/

The **Python half** of the platform. Use Python when the task is "go figure something out
or talk to another system" — parsing, validation, custom logic, and integrations.

## Subpackages

| Folder | Purpose |
|--------|---------|
| `core/` | Connection handling, base classes, device drivers (Nornir / Scrapli / Netmiko) |
| `services/` | Automation workflows — backup, drift detection, compliance audits, reporting |
| `integrations/` | API clients for external systems — NetBox, ServiceNow, monitoring, IPAM |
| `inventory/` | Nornir inventory plugin that reads the shared source of truth |
| `config/` | Settings loader — reads from environment, never hardcodes secrets |
| `utils/` | Shared helpers — logging setup, validators, formatters |

## Import style

```python
from netauto.config import settings
from netauto.services.backup import run_backup
```

Install in editable mode for development: `pip install -e .`
