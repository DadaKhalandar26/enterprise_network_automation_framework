# config/

Settings loader. Reads configuration and secrets from environment variables (or a local
`.env` file), never from hardcoded values.

```python
from netauto.config import settings
settings.netbox_url      # e.g. https://netbox.example.com
settings.netbox_token    # injected from environment, never committed
```

This is the boundary that keeps secrets out of the repo. If you need a new credential,
add it to `.env.example` (placeholder only) and load it here.
