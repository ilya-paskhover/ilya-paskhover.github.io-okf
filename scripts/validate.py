#!/usr/bin/env python3
"""Check an OKF bundle. Usage: python scripts/validate.py [folder]  (default: bundle)"""
import re
import sys
from pathlib import Path

import yaml  # PyYAML: pip install pyyaml

RESERVED = {"index.md", "log.md"}  # OKF gives these names a special job; they are not concepts
FRONTMATTER = re.compile(r"\A---\n(.*?)^---$", re.S | re.M)  # The block between two --- lines
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)")  # Captures the target in [text](target)
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)  # Code samples may look like links, so drop them
EXTERNAL = re.compile(r"[a-z][a-z0-9+.-]*:|#", re.I)  # https:, mailto: or a #same-page link


def frontmatter_problem(text):
    """Return what is wrong with the frontmatter, or None if it has a non-empty type."""
    match = FRONTMATTER.match(text)
    if not match:
        return "no YAML frontmatter at the top of the file"
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as error:
        return f"frontmatter is not valid YAML: {error}"
    kind = data.get("type") if isinstance(data, dict) else None
    if not isinstance(kind, str) or not kind.strip():
        return "frontmatter needs a non-empty type"
    return None


def broken_links(text, path, root):
    """Yield each relative link in the body whose target does not exist."""
    for target in LINK.findall(CODE.sub("", text)):
        if EXTERNAL.match(target):
            continue  # Only links inside the bundle are checked
        clean = target.split("#")[0]
        # In OKF a leading / means "from the bundle root"; otherwise "from this file's folder".
        # shortcut: Windows and macOS ignore filename case, run on Linux for a strict check.
        if not (root / clean[1:] if clean.startswith("/") else path.parent / clean).exists():
            yield target


root = Path(sys.argv[1] if len(sys.argv) > 1 else "bundle")
files = sorted(root.rglob("*.md"))
if not files:
    sys.exit(f"FAIL: no .md files found in {root}")

problems = []
for path in files:
    text = path.read_text(encoding="utf-8")
    if path.name not in RESERVED and (problem := frontmatter_problem(text)):
        problems.append(f"{path}: {problem}")
    problems += [f"{path}: broken link {target}" for target in broken_links(text, path, root)]

print("\n".join(problems) or f"OK: {len(files)} files checked in {root}")
sys.exit(1 if problems else 0)
