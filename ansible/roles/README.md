# ansible/roles/

Reusable automation bundles. Each role is self-contained and applies one logical piece of
configuration (e.g. `base_config`, `interfaces`, `bgp`).

## Standard role layout

```
rolename/
├── tasks/main.yml       # what the role does
├── handlers/main.yml    # actions triggered on change
├── templates/           # role-specific Jinja2 (shared templates live in top-level templates/)
├── defaults/main.yml    # default variables (lowest precedence)
├── vars/main.yml        # role variables
└── meta/main.yml        # role metadata and dependencies
```

Create a role skeleton with: `ansible-galaxy init rolename`

Roles should be idempotent — running them repeatedly produces the same result. Test them
with Molecule (see `tests/molecule/`).
