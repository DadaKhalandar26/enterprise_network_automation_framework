# core/

The plumbing. Defines how the platform connects to devices and the base classes that
services build on.

- Connection drivers (Scrapli for speed, Netmiko for broad compatibility, NAPALM for
  structured data).
- Nornir runner setup and base task classes.
- Shared abstractions inherited by everything in `services/`.

Keep vendor-specific connection quirks here so services stay vendor-agnostic.
