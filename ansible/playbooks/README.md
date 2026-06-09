# ansible/playbooks/

Playbooks orchestrate roles into complete workflows. Think of playbooks as the conductor
and roles as the musicians.

## Typical playbooks

- **`site.yml`** — Top-level orchestration. Applies base config, then services (BGP,
  interfaces, etc.), then validation, in order.
- **`provision.yml`** — Onboard a new device end to end.
- **`backup.yml`** — Pull running configs from devices and save them.
- **`compliance.yml`** — Check live configs against the golden baseline and flag drift.

## Convention

Keep playbooks thin — they should call roles, not contain large blocks of inline tasks.
Logic belongs in roles so it can be reused and tested with Molecule.
