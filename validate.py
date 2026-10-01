#!/usr/bin/env python3
"""Check registry.json: the schema, unique ids in id order, and each entry
against its plugin's own manifest on GitHub (same id and name, an engines
range that starts at minHost). Needs the `jsonschema` package; `--offline`
skips the GitHub checks."""
import json
import sys
import urllib.request
from pathlib import Path

from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parent
registry = json.loads((root / "registry.json").read_text())
schema = json.loads((root / "registry.schema.json").read_text())
problems = [f"{'/'.join(map(str, e.path))}: {e.message}" for e in Draft202012Validator(schema).iter_errors(registry)]
ids = [p["id"] for p in registry.get("plugins", [])]
if len(ids) != len(set(ids)):
    problems.append("plugin ids must be unique")
if ids != sorted(ids):
    problems.append("entries must be sorted by id")
if "--offline" not in sys.argv:
    for entry in registry.get("plugins", []):
        url = f"https://raw.githubusercontent.com/{entry['repo']}/HEAD/super-desktop-plugin.json"
        try:
            with urllib.request.urlopen(url, timeout=20) as response:
                manifest = json.load(response)
        except Exception as error:  # report every entry, then fail
            problems.append(f"{entry['id']}: cannot read {url}: {error}")
            continue
        if manifest.get("id") != entry["id"] or manifest.get("name") != entry["name"]:
            problems.append(f"{entry['id']}: id/name differ from the plugin's manifest ({manifest.get('id')}, {manifest.get('name')})")
        if not manifest.get("engines", {}).get("superDesktop", "").startswith(f">={entry['minHost']}"):
            problems.append(f"{entry['id']}: minHost {entry['minHost']} does not match engines.superDesktop {manifest.get('engines', {}).get('superDesktop')}")
for problem in problems:
    print("problem:", problem)
print(f"{len(ids)} plugin(s), {len(problems)} problem(s)")
sys.exit(1 if problems else 0)
