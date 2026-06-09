# scripts/

Operational one-offs and entry points — thin wrappers that invoke the package or Ansible.

Examples:
- `run_backup.py` — import and run the backup service.
- `compliance_check.py` — run drift detection, trigger a remediation playbook if needed.
- `deploy.sh` — convenience wrapper around `ansible-playbook`.

Keep real logic in `src/netauto/` and roles; scripts should just orchestrate and pass
arguments. Most are also exposed through the `Makefile`.
