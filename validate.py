#!/usr/bin/env python3
"""Check registry.json: the schema, unique ids in id order, and each entry
against its plugin's own plugin.json on GitHub (same id, name and api, the
same slots); a missing preview.png is a note, not a problem. Needs the `jsonschema` package; `--offline` skips GitHub."""
import json
import sys
import urllib.request
from pathlib import Path

from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parent
registry = json.loads((root / "registry.json").read_text())
schema = json.loads((root / "registry.schema.json").read_text())
problems = [f"{'/'.join(map(str, e.path))}: {e.message}" for e in Draft202012Validator(schema).iter_errors(registry)]
plugins = registry.get("plugins", [])
ids = [p.get("id") for p in plugins]
if len(ids) != len(set(ids)):
    problems.append("plugin ids must be unique")
if ids != sorted(ids, key=str):
    problems.append("entries must be sorted by id")
for entry in plugins:
    if "slots" in entry and entry["slots"] != sorted(entry["slots"]):
        problems.append(f"{entry.get('id')}: slots must be sorted")
if "--offline" not in sys.argv:
    for entry in plugins:
        url = f"https://raw.githubusercontent.com/{entry['repo']}/HEAD/plugin.json"
        try:
            with urllib.request.urlopen(url, timeout=20) as response:
                manifest = json.load(response)
        except Exception as error:  # report every entry, then fail
            problems.append(f"{entry['id']}: cannot read {url}: {error}")
            continue
        for field in ("id", "name", "api"):
            if manifest.get(field) != entry.get(field):
                problems.append(f"{entry['id']}: {field} {entry.get(field)!r} differs from plugin.json ({manifest.get(field)!r})")
        preview = f"https://raw.githubusercontent.com/{entry['repo']}/HEAD/preview.png"
        try:
            with urllib.request.urlopen(urllib.request.Request(preview, method="HEAD"), timeout=20):
                pass
        except Exception:  # not required: SUPER DESKTOP shows a placeholder
            print(f"note: {entry['id']}: no preview.png at the top of {entry['repo']}")
        slots = sorted({s.get("slot") for s in manifest.get("surfaces", [])})
        if "slots" in entry and entry["slots"] != slots:
            problems.append(f"{entry['id']}: slots {entry['slots']} differ from plugin.json ({slots})")
for problem in problems:
    print("problem:", problem)
print(f"{len(ids)} plugin(s), {len(problems)} problem(s)")
sys.exit(1 if problems else 0)
