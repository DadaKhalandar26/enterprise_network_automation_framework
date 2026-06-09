# ansible/collections/

External Ansible collections this project depends on.

- **`requirements.yml`** — Declares the collections to install, e.g. `cisco.ios`,
  `arista.eos`, `junipernetworks.junos`. These provide the modules that know how to talk
  to each vendor's devices.

## Install

```bash
ansible-galaxy collection install -r requirements.yml
```

Pin versions in `requirements.yml` for reproducible builds. Do not commit installed
collection files — only the `requirements.yml` manifest.
