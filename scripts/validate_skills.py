#!/usr/bin/env python3
"""
Validate skill directory structure and SKILL.md frontmatter.

Zero external dependencies — uses only Python standard library.
Exit code 0: all checks passed (warnings are OK).
Exit code 1: at least one ERROR found.

Usage:
    python scripts/validate_skills.py                # scan default ./skills/
    python scripts/validate_skills.py --path PATH    # scan specific dir

Inspired by MiniMax-AI/skills/.claude/skills/pr-review/scripts/validate_skills.py (MIT).
"""

import argparse
import os
import re
import sys


def extract_frontmatter(text):
    """提取 --- 之间的 YAML frontmatter。"""
    stripped = text.lstrip("﻿")
    if not stripped.startswith("---"):
        return None
    end = stripped.find("---", 3)
    if end == -1:
        return None
    return stripped[3:end]


def parse_frontmatter_fields(fm_text):
    """简单 YAML 解析——只处理顶层标量字段。"""
    fields = {}
    for line in fm_text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(.*)", line)
        if m:
            key = m.group(1)
            value = m.group(2).strip().strip("\"'")
            fields[key] = value
    return fields


SECRET_PATTERNS = [
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI-style API key"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key"),
    (r"Bearer\s+[a-zA-Z0-9_\-\.]{50,}", "Hardcoded bearer token"),
    (r"AIza[0-9A-Za-z_\-]{35}", "Google API key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub personal access token"),
]

SCAN_EXTENSIONS = {".md", ".py", ".sh", ".js", ".ts", ".json", ".yaml", ".yml", ".txt"}


def scan_secrets(filepath):
    """扫描文件里的硬编码 secret。"""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        return []
    findings = []
    for line_no, line in enumerate(content.splitlines(), 1):
        for pattern, desc in SECRET_PATTERNS:
            for match in re.finditer(pattern, line):
                findings.append((line_no, desc, match.group(0)[:60]))
    return findings


def find_skill_dirs(base_path):
    """找含 SKILL.md 的目录。"""
    skill_dirs = []
    for root, dirs, files in os.walk(base_path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        if "SKILL.md" in files:
            skill_dirs.append(root)
    return sorted(skill_dirs)


def validate_skill(skill_dir):
    """验证单个 skill 目录。返回 (errors, warnings)。"""
    errors = []
    warnings = []
    dir_name = os.path.basename(skill_dir)
    skill_md = os.path.join(skill_dir, "SKILL.md")

    with open(skill_md, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    fm_text = extract_frontmatter(content)
    if fm_text is None:
        errors.append("SKILL.md missing YAML frontmatter (no --- markers)")
        return errors, warnings

    fields = parse_frontmatter_fields(fm_text)

    name = fields.get("name", "").strip()
    if not name:
        errors.append("missing required field: name")
    elif name != dir_name:
        errors.append(f"name '{name}' does not match directory '{dir_name}'")

    desc = fields.get("description", "").strip()
    if not desc:
        errors.append("missing required field: description")
    elif len(desc) < 30:
        warnings.append(f"description too short ({len(desc)} chars) - should include trigger conditions for the agent")

    if "license" not in fields:
        warnings.append("missing recommended field: license")

    # 扫描所有文件的 secret
    for root, dirs, files in os.walk(skill_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in SCAN_EXTENSIONS:
                continue
            filepath = os.path.join(root, fname)
            findings = scan_secrets(filepath)
            for line_no, sdesc, matched in findings:
                rel = os.path.relpath(filepath, skill_dir)
                errors.append(f"{rel}:{line_no} possible hardcoded secret ({sdesc}): {matched}")

    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description="Validate skill structure and frontmatter")
    ap.add_argument("--path", default="skills", help="扫描路径，默认 ./skills/")
    args = ap.parse_args()

    if not os.path.isdir(args.path):
        print(f"ERROR: path does not exist: {args.path}")
        sys.exit(1)

    skill_dirs = find_skill_dirs(args.path)
    if not skill_dirs:
        print(f"WARN: no SKILL.md found under {args.path}")
        sys.exit(0)

    total_errors = 0
    total_warnings = 0

    for skill_dir in skill_dirs:
        errors, warnings = validate_skill(skill_dir)
        rel = os.path.relpath(skill_dir)
        if not errors and not warnings:
            print(f"OK  {rel}")
        else:
            print(f"--- {rel}")
            for e in errors:
                print(f"   ERROR: {e}")
                total_errors += 1
            for w in warnings:
                print(f"   WARN:  {w}")
                total_warnings += 1

    print()
    print(f"Summary: {len(skill_dirs)} skill(s), {total_errors} error(s), {total_warnings} warning(s)")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
