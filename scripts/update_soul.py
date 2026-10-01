#!/usr/bin/env python3
import argparse
import base64
import hashlib
import json
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


def block_span(data):
    if not data.count(BEGIN) and not data.count(END):
        return None
    if data.count(BEGIN) != 1 or data.count(END) != 1:
        raise ValueError("Incomplete or duplicate policy markers; file unchanged")
    start, finish = data.index(BEGIN), data.index(END)
    if finish < start:
        raise ValueError("Reversed policy markers; file unchanged")
    return start, finish + len(END)


def replace_block(original, block):
    span = block_span(original)
    if span:
        start, finish = span
        return original[:start] + block + original[finish:]
    separator = b"" if not original or original.endswith(b"\n") else b"\n"
    return original + separator + block + b"\n"


def project_paths(project_root, state_dir=None):
    root = Path(project_root).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project root must be an existing directory")
    target = root / "Soul.md"
    if target.is_symlink():
        raise ValueError("Soul.md is a symlink; review its destination before editing")
    directory = Path(state_dir).expanduser().resolve() if state_dir else Path.home() / '.codex' / 'lean-build-state'
    if directory == root or root in directory.parents:
        raise ValueError("Snapshot directory must be outside the target project")
    key = hashlib.sha256(str(root).encode()).hexdigest()
    return root, target, directory / (key + '.json')


def decode(value):
    return base64.b64decode(value, validate=True)


def restore_content(current, state):
    before, applied = decode(state['before']), decode(state['applied'])
    if current == applied or current == before:
        return before
    span, applied_span, before_span = block_span(current), block_span(applied), block_span(before)
    if not span or not applied_span:
        raise ValueError("Owned policy is missing; restoration not completed")
    start, finish = span
    if current[start:finish] != applied[applied_span[0]:applied_span[1]]:
        raise ValueError("Owned policy changed outside the skill; restoration not completed")
    if before_span:
        return current[:start] + before[before_span[0]:before_span[1]] + current[finish:]
    lead = b"" if not before or before.endswith(b"\n") else b"\n"
    if lead and current[max(0, start - len(lead)):start] == lead:
        start -= len(lead)
    if current[finish:finish + 1] == b"\n":
        finish += 1
    return current[:start] + current[finish:]


def read_state(snapshot, root):
    state = json.loads(snapshot.read_text())
    if state['root'] != str(root):
        raise ValueError("Snapshot belongs to a different project")
    return state


def write_verified(target, data, existed=True):
    if not existed and not data:
        if target.exists():
            target.unlink()
        if target.exists():
            raise OSError("File removal verification failed")
        return
    if not target.exists() or target.read_bytes() != data:
        target.write_bytes(data)
    if target.read_bytes() != data:
        raise OSError("Soul.md read-back verification failed")


def update_soul(project_root, mode, state_dir=None):
    root, target, snapshot = project_paths(project_root, state_dir)
    current = target.read_bytes() if target.exists() else b""
    block = render_block(mode)
    if snapshot.exists():
        state = read_state(snapshot, root)
        baseline = restore_content(current, state)
    else:
        baseline = current
        state = {'root': str(root), 'existed': target.exists(),
                 'before': base64.b64encode(current).decode()}
    updated = replace_block(baseline, block)
    state['applied'] = base64.b64encode(updated).decode()
    snapshot.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    snapshot.write_text(json.dumps(state, indent=2) + '\n')
    snapshot.chmod(0o600)
    if read_state(snapshot, root) != state:
        raise OSError("Baseline read-back verification failed")
    write_verified(target, updated)
    return target, current != updated


def disable_skill(project_root, state_dir=None):
    root, target, snapshot = project_paths(project_root, state_dir)
    current = target.read_bytes() if target.exists() else b""
    if not snapshot.exists():
        if block_span(current):
            raise ValueError("No pre-activation baseline for legacy policy; restoration not completed")
        return target, False
    state = read_state(snapshot, root)
    restored = restore_content(current, state)
    was_present = target.exists()
    write_verified(target, restored, state['existed'])
    snapshot.unlink()
    return target, current != restored or was_present != target.exists()


def main():
    parser = argparse.ArgumentParser(description="Apply or restore lean-build project settings")
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--state-dir")
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument("--mode", choices=MODES)
    operation.add_argument("--disable-skill", action='store_true')
    args = parser.parse_args()
    try:
        if args.disable_skill:
            disable_skill(args.project_root, args.state_dir)
            message = 'Original project settings restored and verified.'
        else:
            update_soul(args.project_root, args.mode, args.state_dir)
            message = 'Project settings applied and verified.'
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Operation not completed: {error}\n")
    print(message)


if __name__ == "__main__":
    main()
