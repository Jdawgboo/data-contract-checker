# Data Contract Checker

Validate JSON-like records against a small declared requiredness and type contract.

```bash
cat payload.json | python tool.py
python -m unittest -v
```

Supported types are `str`, `int`, `float`, `bool`, `list`, and `dict`. This intentionally supports a compact local contract subset, not the full JSON Schema specification.
