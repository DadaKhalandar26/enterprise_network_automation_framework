# ansible/

The **declarative half** of the platform. Use Ansible when the task is "make the device
match this declared state" — config push, provisioning, idempotent changes.

## Layout

- **`ansible.cfg`** — Ansible settings (inventory path, roles path, SSH options).
- **`playbooks/`** — Orchestration. Playbooks tie roles together into workflows.
- **`roles/`** — Reusable, self-contained automation bundles (tasks, handlers, templates, defaults).
- **`collections/requirements.yml`** — External collections this project depends on
  (e.g. `cisco.ios`, `arista.eos`, `junipernetworks.junos`).
- **`group_vars/` / `host_vars/`** — Ansible-specific variables only. Shared device data
  should live in the top-level `inventory/` source of truth instead.

## Usage

```bash
ansible-galaxy collection install -r collections/requirements.yml
ansible-playbook playbooks/site.yml
ansible-playbook playbooks/backup.yml --limit core-switches
```

Inventory is read from the shared top-level `inventory/` directory (NetBox dynamic
inventory or the static fallback), so Ansible and the Python stack see identical devices.
