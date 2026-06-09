# configs/

Device configuration artifacts.

- **`golden/`** — The intended baseline (golden) configs. **Committed** to version
  control. These represent what each device *should* look like and are the reference for
  compliance and drift detection.
- **`rendered/`** — Machine-generated configs produced during runs. **Gitignored** —
  never commit generated output.

Splitting intended (`golden/`) from generated (`rendered/`) is what enables config drift
detection: services compare live device config against `golden/`.
