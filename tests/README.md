# tests/

Automated tests for both stacks. Run via `make test`.

## Layout

- **`unit/`** — `pytest` tests for the Python package. Network calls are mocked so tests
  run anywhere without devices.
- **`molecule/`** — Molecule scenarios for testing Ansible roles. Spins up a test target
  (container/VM), applies a role, and verifies the result.
- **`integration/`** — End-to-end tests against lab devices or simulators (GNS3 / CML).
- **`fixtures/`** — Sample device outputs and mock data shared across tests.

## Run

```bash
pytest tests/unit
molecule test            # from within a role directory
```
