# inventory/ (Python)

The Nornir inventory plugin. Reads from the **same** source of truth the Ansible stack
uses (the top-level `inventory/` directory — NetBox dynamic inventory or static fallback),
so both stacks see identical devices and variables.

This is *not* the device list itself — that lives in the top-level `inventory/`. This is
the code that loads it into Nornir.
