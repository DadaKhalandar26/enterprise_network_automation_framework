# inventory/

The **shared source of truth** for both Ansible and Python. Defines which devices are
managed and the variables describing them. Both stacks read from here, so there is one
authoritative device list.

## Contents

- **`netbox.yml`** — Dynamic inventory configuration. Pulls live device data from NetBox
  and feeds both Ansible (`netbox.netbox.nb_inventory`) and the Nornir plugin.
- **`hosts.yml`** — Static inventory fallback for labs or when NetBox is unavailable.
- **`group_vars/`** — Variables applied to groups of devices (e.g. `all.yml` for global
  settings like NTP servers).
- **`host_vars/`** — Variables for individual devices.

## Principle

Let NetBox be the authority. Add a device once (in NetBox) and both stacks pick it up
automatically — no duplicated lists, no drift.
