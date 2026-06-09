# templates/

Shared Jinja2 templates — the blueprints for device configuration. Both Ansible (the
`template` module) and the Python stack render these same files, so config logic lives in
one place.

## Layout

Organized by platform/vendor:

```
templates/
├── cisco_ios/
├── arista_eos/
└── juniper_junos/
```

## Convention

Keep templates **tool-agnostic** — avoid Ansible-only filters in templates you also render
from Python. Variables are supplied from the shared `inventory/` source of truth.
