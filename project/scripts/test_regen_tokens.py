#!/usr/bin/env python3
"""
Regression test for regen_tokens.py. Run after any change to that script or to
project/tokens.json:

    python3 project/scripts/test_regen_tokens.py

Checks:
  1. The generator runs clean on the current source.
  2. Every JSON export is valid JSON and every leaf token carries $type/$value.
  3. Running it twice produces byte-identical JSON (idempotency) -- the
     tokens.css header timestamp is the one allowed exception.
  4. --check reports "in sync" immediately after a regen, and reports "STALE"
     when the source changes without a re-run.
"""
import json, pathlib, subprocess, sys, tempfile, shutil, hashlib

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[2]
PROJECT = ROOT / "project"
EXPORT = ROOT / "export"
SCRIPT = HERE.parent / "regen_tokens.py"
SRC = PROJECT / "tokens.json"

JSON_FILES = ["tokens.light.json", "tokens.dark.json", "typography.json", "motion.json"]

failures = []


def check(label, cond):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {label}")
    if not cond:
        failures.append(label)


def run_generator():
    r = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    return r.returncode == 0, r.stdout, r.stderr


def walk_leaves(obj):
    """Yield every dict in the tree that looks like a token leaf ($value present)."""
    if isinstance(obj, dict):
        if "$value" in obj:
            yield obj
        else:
            for v in obj.values():
                yield from walk_leaves(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_leaves(v)


def main():
    ok, out, err = run_generator()
    check("generator runs without error", ok)
    if not ok:
        print(err)
        sys.exit(1)

    for name in JSON_FILES:
        path = EXPORT / name
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            valid = True
        except Exception as e:
            valid = False
            data = None
        check(f"{name} is valid JSON", valid)
        if valid:
            leaves = list(walk_leaves(data))
            all_typed = all("$type" in leaf for leaf in leaves)
            check(f"{name}: every leaf token has $type ({len(leaves)} leaves)", all_typed)

    # idempotency
    before = {n: hashlib.sha256((EXPORT / n).read_bytes()).hexdigest() for n in JSON_FILES}
    ok2, _, _ = run_generator()
    check("second run also succeeds", ok2)
    after = {n: hashlib.sha256((EXPORT / n).read_bytes()).hexdigest() for n in JSON_FILES}
    check("JSON exports are byte-identical across two runs (idempotent)", before == after)

    # --check mode
    r = subprocess.run([sys.executable, str(SCRIPT), "--check"], cwd=ROOT, capture_output=True, text=True)
    check("--check reports in-sync right after a regen", r.returncode == 0)

    with tempfile.TemporaryDirectory() as tmp:
        backup = pathlib.Path(tmp) / "tokens.json.bak"
        shutil.copy(SRC, backup)
        try:
            original = SRC.read_text(encoding="utf-8")
            SRC.write_text(original.replace('"version": 1', '"version": 1 '), encoding="utf-8")  # trivial byte change
            r = subprocess.run([sys.executable, str(SCRIPT), "--check"], cwd=ROOT, capture_output=True, text=True)
            check("--check reports STALE after an un-regenerated source edit", r.returncode == 1)
        finally:
            shutil.copy(backup, SRC)
            run_generator()  # restore export/ to match the real source again

    print()
    if failures:
        print(f"{len(failures)} check(s) FAILED:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("All checks passed.")


if __name__ == "__main__":
    main()
