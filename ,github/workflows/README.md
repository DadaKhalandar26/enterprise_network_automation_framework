# .github/workflows

GitHub Actions workflow definitions. GitHub automatically detects and runs any `.yml`
file placed here.

## Files

- **`ci.yml`** — Continuous integration. Runs on every push and pull request. Installs
  the linters and runs them against the codebase (`yamllint`, `ruff`, `black`,
  `ansible-lint`) plus the test suite. If any step fails, the workflow fails and the
  pull request is blocked from merging. This is the automated quality gate.

- **`deploy.yml`** — Deployment. Triggered **manually only** via `workflow_dispatch`,
  never on push. Installs Ansible and the required collections, then runs the playbooks
  against devices. Protected by an `environment: production` rule that requires a human
  reviewer to approve before anything touches the network.

## Key concept

Two things keep deployments safe: `workflow_dispatch` (manual trigger, no auto-run) and
the protected `production` environment (required approval). Configure reviewers under
repo **Settings → Environments → production**.

## Reference

Workflow syntax: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions
