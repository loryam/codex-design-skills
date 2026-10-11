#!/usr/bin/env python3
"""
Scan a frontend repository for common design drift indicators.

This script is intentionally conservative: it flags possible issues for review;
it does not prove that every match is wrong.

Usage:
  python .agents/skills/ui-consistency-guardian/scripts/audit_design_consistency.py .
  python .agents/skills/ui-consistency-guardian/scripts/audit_design_consistency.py ./src --format markdown
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

TEXT_EXTENSIONS = {
    ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html",
    ".css", ".scss", ".sass", ".less", ".mdx"
}

IGNORED_DIRS = {
    ".git", ".next", ".nuxt", ".svelte-kit", "node_modules", "dist", "build",
    "coverage", ".turbo", ".cache", "vendor", "out", "storybook-static"
}

TOKEN_FILE_HINTS = (
    "token", "theme", "tailwind.config", "variables", "global", "globals", "design-system"
)

PATTERNS = {
    "raw_hex_color": re.compile(r"(?<![A-Za-z0-9_-])#[0-9a-fA-F]{3,8}\b"),
    "raw_rgb_hsl_color": re.compile(r"\b(?:rgb|rgba|hsl|hsla)\s*\([^\)]*\)", re.IGNORECASE),
    "arbitrary_tailwind_value": re.compile(r"\b(?:text|bg|border|ring|from|to|via|p|px|py|pt|pr|pb|pl|m|mx|my|mt|mr|mb|ml|gap|w|h|min-w|min-h|max-w|max-h|rounded|shadow|leading|tracking)-\[[^\]]+\]"),
    "inline_style_prop": re.compile(r"\bstyle=\{\{|\bstyle=\""),
    "font_size_px": re.compile(r"font-size\s*:\s*\d+(?:\.\d+)?px", re.IGNORECASE),
    "line_height_px": re.compile(r"line-height\s*:\s*\d+(?:\.\d+)?px", re.IGNORECASE),
    "font_family_literal": re.compile(r"font-family\s*:\s*[^;]+;", re.IGNORECASE),
    "important_css": re.compile(r"!important\b"),
}

@dataclass
class Finding:
    file: str
    line: int
    kind: str
    value: str
    note: str


def is_probably_token_file(path: Path) -> bool:
    lower = str(path).lower()
    return any(hint in lower for hint in TOKEN_FILE_HINTS)


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS:
            yield path


def scan_file(path: Path, root: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return findings

    rel = str(path.relative_to(root))
    token_file = is_probably_token_file(path)

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("//") or stripped.startswith("/*"):
            continue

        for kind, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                value = match.group(0).strip()
                note = "Review for design-system consistency."

                if kind in {"raw_hex_color", "raw_rgb_hsl_color", "font_family_literal"} and token_file:
                    note = "Allowed in token/theme/global files if this is a source-of-truth value."
                elif kind == "arbitrary_tailwind_value":
                    note = "Prefer theme tokens/classes over arbitrary Tailwind values unless intentionally documented."
                elif kind == "inline_style_prop":
                    note = "Prefer classes/tokens for static visual styling; inline style may be acceptable for dynamic values."
                elif kind in {"font_size_px", "line_height_px"}:
                    note = "Prefer typography tokens, CSS variables, or semantic text variants."
                elif kind == "important_css":
                    note = "Avoid !important unless overriding third-party CSS with documented reason."

                findings.append(Finding(rel, line_no, kind, value, note))

    return findings


def to_markdown(findings: list[Finding]) -> str:
    if not findings:
        return "# Design consistency audit\n\nNo common design drift indicators found.\n"

    lines = ["# Design consistency audit", "", f"Found {len(findings)} potential issue(s).", ""]
    grouped: dict[str, list[Finding]] = {}
    for finding in findings:
        grouped.setdefault(finding.kind, []).append(finding)

    for kind, items in grouped.items():
        lines.extend([f"## {kind}", ""])
        for item in items[:100]:
            lines.append(f"- `{item.file}:{item.line}` — `{item.value}` — {item.note}")
        if len(items) > 100:
            lines.append(f"- …and {len(items) - 100} more `{kind}` finding(s).")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan for UI design consistency drift.")
    parser.add_argument("root", nargs="?", default=".", help="Repository or source directory to scan.")
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--output", help="Optional output file path.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"Path does not exist: {root}")

    findings: list[Finding] = []
    for file_path in iter_files(root):
        findings.extend(scan_file(file_path, root))

    if args.format == "json":
        output = json.dumps([asdict(f) for f in findings], indent=2)
    else:
        output = to_markdown(findings)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output)

    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
