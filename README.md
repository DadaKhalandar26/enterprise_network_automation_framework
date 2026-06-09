# Enterprise Network Automation

A hybrid network automation platform combining **Ansible** (declarative configuration
push and orchestration) and **Python** (Nornir / Netmiko / NAPALM / Scrapli for parsing,
validation, and integrations), driven by a single source of truth.

---

## What this project does

| Stack | Responsibility | Examples |
|-------|----------------|----------|
| **Ansible** | "Make the device match this declared state" | Config push, provisioning, idempotent changes |
| **Python** | "Go figure something out / talk to other systems" | Drift detection, parsing, NetBox & ServiceNow workflows |

Both stacks read the **same inventory / source of truth** and render the **same Jinja2
templates**, so the two halves never disagree about what devices exist or how they should
be configured.

---

## Repository structure

```
enterprise-network-automation/
├── .github/workflows/   # CI/CD pipelines (lint, test, gated deploy)
├── ansible/             # Playbooks, roles, collections — the declarative half
├── src/netauto/         # Python package — parsing, validation, integrations
├── inventory/           # Shared source of truth (NetBox dynamic + static fallback)
├── templates/           # Shared Jinja2 config templates, by platform
├── configs/             # golden/ (intended baseline) + rendered/ (generated, ignored)
├── tests/               # pytest (unit) + molecule (Ansible roles)
├── scripts/             # Operational one-offs and entry points
├── docs/                # Project documentation
├── logs/                # Runtime logs (gitignored)
├── reports/             # Generated reports (gitignored)
├── .env.example         # Required env vars — NO real values
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements.txt
├── Makefile
├── README.md
└── LICENSE
```

Each folder contains its own `README.md` explaining its purpose and conventions.

---

## Getting started

```bash
# 1. Clone
git clone https://github.com/<you>/enterprise-network-automation.git
cd enterprise-network-automation

# 2. Python environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Ansible collections
ansible-galaxy collection install -r ansible/collections/requirements.yml

# 4. Configure secrets (never commit these)
cp .env.example .env
# edit .env with your NetBox URL/token, device creds, etc.

# 5. Verify everything lints
make lint
```

---

## Secrets handling

**Secrets never live in the repo.** The repo describes *what* config is needed; the
environment supplies the *values*.

- `.env.example` (committed) shows the required variables with placeholder values.
- `.env` (gitignored) holds your real values locally.
- In CI/CD, values come from **GitHub repo secrets** (Settings → Secrets and variables).
- For production, an external secrets manager (HashiCorp Vault, AWS/Azure Secrets) is
  recommended so both Python and Ansible read from one place.

A `gitleaks` pre-commit hook blocks accidental credential commits.

---

## CI/CD

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `ci.yml` | Every push / pull request | Runs `yamllint`, `ruff`, `black`, `ansible-lint`, and the test suite. Blocks merge on failure. |
| `deploy.yml` | Manual (`workflow_dispatch`) only | Runs Ansible playbooks against devices, gated behind a required-reviewer approval. Never auto-deploys. |

---

## Common commands

```bash
make lint      # run all linters
make test      # run pytest + molecule
make backup    # run the Python backup service
make deploy    # trigger a (gated) deployment
```

---

## Contributing

1. Branch off `main`.
2. Make changes; run `make lint` and `make test` locally.
3. Open a pull request — `ci.yml` runs automatically.
4. Deployments to devices happen only through the gated `deploy.yml` workflow.

## License

See [LICENSE](LICENSE).
