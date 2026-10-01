#!/usr/bin/env python3
import argparse
from pathlib import Path


BEGIN = b"<!-- defensive-construction:begin -->"
END = b"<!-- defensive-construction:end -->"
MODES = ("Enable", "Low", "Disable")


def render_block(mode):
    if mode not in MODES:
        raise ValueError("Invalid mode")
    source = Path(__file__).resolve().parents[1] / "references" / "persistence.md"
    template = source.read_bytes()
    start = template.index(BEGIN)
    finish = template.index(END, start) + len(END)
    block = template[start:finish]
    if block.count(b"Mode: Low") != 1:
        raise ValueError("Invalid policy template")
    return block.replace(b"Mode: Low", f"Mode: {mode}".encode(), 1)


def replace_block(original, block):
    if not original.count(BEGIN) and not original.count(END):
        separator = b"" if not original or original.endswith(b"\n") else b"\n"
        return original + separator + block + b"\n"
    if original.count(BEGIN) != 1 or original.count(END) != 1:
        raise ValueError("Incomplete or duplicate policy markers; file unchanged")
    start = original.index(BEGIN)
    finish = original.index(END)
    if finish < start:
        raise ValueError("Reversed policy markers; file unchanged")
    return original[:start] + block + original[finish + len(END):]


def update_soul(project_root, mode):
    root = Path(project_root).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project root must be an existing directory")
    target = root / "Soul.md"
    if target.is_symlink():
        raise ValueError("Soul.md is a symlink; review its destination before editing")
    original = target.read_bytes() if target.exists() else b""
    updated = replace_block(original, render_block(mode))
    if updated != original:
        target.write_bytes(updated)
    if target.read_bytes() != updated:
        raise OSError("Soul.md read-back verification failed")
    return target, updated != original


def main():
    parser = argparse.ArgumentParser(description="Update the lean-build block in project-root Soul.md")
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--mode", required=True, choices=MODES)
    args = parser.parse_args()
    try:
        target, changed = update_soul(args.project_root, args.mode)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Policy not saved: {error}\n")
    print(f"Policy {'saved' if changed else 'unchanged'} and verified: {target}")


if __name__ == "__main__":
    main()
