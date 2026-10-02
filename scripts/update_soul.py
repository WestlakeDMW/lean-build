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
    return template[start:finish].replace(b"Mode: Low", f"Mode: {mode}".encode(), 1)


def block_span(data):
    if not data.count(BEGIN) and not data.count(END):
        return None
    if data.count(BEGIN) != 1 or data.count(END) != 1:
        raise ValueError("Incomplete or duplicate prompt markers; file unchanged")
    start, finish = data.index(BEGIN), data.index(END)
    if finish < start:
        raise ValueError("Reversed prompt markers; file unchanged")
    return start, finish + len(END)


def edit_prompt(project_root, mode=None):
    root = Path(project_root).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project root must be an existing directory")
    target = root / "Soul.md"
    if target.is_symlink():
        raise ValueError("Review the Soul.md symlink destination before editing")
    original = target.read_bytes() if target.exists() else b""
    span = block_span(original)
    if mode is None:
        if not span:
            return target, False
        start, finish = span
        updated = original[:start] + original[finish:]
    else:
        block = render_block(mode)
        if span:
            start, finish = span
            updated = original[:start] + block + original[finish:]
        else:
            separator = b"" if not original or original.endswith(b"\n") else b"\n"
            updated = original + separator + block + b"\n"
    if updated != original or not target.exists():
        target.write_bytes(updated)
    if target.read_bytes() != updated:
        raise OSError("Soul.md read-back verification failed")
    return target, updated != original


def main():
    parser = argparse.ArgumentParser(description="Add, update, or remove the lean-build prompt")
    parser.add_argument("--project-root", required=True)
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument("--mode", choices=MODES)
    operation.add_argument("--disable-skill", action="store_true")
    args = parser.parse_args()
    try:
        edit_prompt(args.project_root, args.mode)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Operation not completed: {error}\n")
    print("Prompt removal verified." if args.disable_skill else "Prompt update verified.")


if __name__ == "__main__":
    main()
