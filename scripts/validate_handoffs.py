#!/usr/bin/env python3
"""Validate executable recommendation handoffs without third-party packages."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECOMMENDATION_GLOB = "sites/*/recommendations/*.md"
START = "<!-- ACTIVE_SCOPE_START -->"
END = "<!-- ACTIVE_SCOPE_END -->"


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    closing = text.find("\n---\n", 4)
    if closing == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:closing].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def active_scope(text: str) -> str | None:
    if text.count(START) != 1 or text.count(END) != 1:
        return None
    start = text.index(START) + len(START)
    end = text.index(END, start)
    return text[start:end].strip("\n") + "\n"


def queue_entries(index_text: str) -> list[tuple[str, int]]:
    start_marker = "<!-- EXECUTION_QUEUE_START -->"
    end_marker = "<!-- EXECUTION_QUEUE_END -->"
    if start_marker not in index_text or end_marker not in index_text:
        return []
    block = index_text.split(start_marker, 1)[1].split(end_marker, 1)[0]
    return [
        (task_id, int(version))
        for task_id, version in re.findall(
            r"`([A-Z]{2,4}-\d{4})`\s+—\s+prompt version\s+(\d+)", block
        )
    ]


def main() -> int:
    errors: list[str] = []
    approved: dict[str, tuple[int, Path]] = {}

    for path in sorted(ROOT.glob(RECOMMENDATION_GLOB)):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("status") != "approved":
            continue

        task_id = meta.get("task_id", "")
        if not re.fullmatch(r"[A-Z]{2,4}-\d{4}", task_id):
            errors.append(f"{path}: approved task has invalid task_id {task_id!r}")
            continue
        if task_id in approved:
            errors.append(f"{path}: duplicate approved task_id {task_id}")
            continue
        try:
            version = int(meta.get("prompt_version", ""))
        except ValueError:
            errors.append(f"{path}: approved task has invalid prompt_version")
            continue

        scope = active_scope(text)
        if scope is None:
            errors.append(f"{path}: approved task needs exactly one active-scope block")
            continue

        expected = "sha256:" + hashlib.sha256(scope.encode("utf-8")).hexdigest()
        actual = meta.get("scope_fingerprint")
        if actual != expected:
            errors.append(
                f"{path}: scope_fingerprint mismatch\n  actual:   {actual}\n  expected: {expected}"
            )

        item_ids = sorted(set(re.findall(rf"{re.escape(task_id)}-[A-Z0-9]+", scope)))
        if not item_ids:
            errors.append(f"{path}: active scope has no stable item IDs")
        if f"Prompt version: {version}" not in scope:
            errors.append(f"{path}: active scope does not declare prompt version {version}")
        if "## Active execution scope" not in text:
            errors.append(f"{path}: missing Active execution scope heading")
        for heading in ("## Final decision", "## Implementation prompt", "## Acceptance criteria"):
            if heading not in text:
                errors.append(f"{path}: missing {heading}")

        approved[task_id] = (version, path)

    queued: dict[str, tuple[int, Path]] = {}
    for index_path in sorted(ROOT.glob("sites/*/recommendations/index.md")):
        for task_id, version in queue_entries(index_path.read_text(encoding="utf-8")):
            if task_id in queued:
                errors.append(f"{index_path}: duplicate queued task {task_id}")
            queued[task_id] = (version, index_path)

    if set(approved) != set(queued):
        missing = sorted(set(approved) - set(queued))
        stale = sorted(set(queued) - set(approved))
        if missing:
            errors.append(f"approved tasks missing from execution queue: {', '.join(missing)}")
        if stale:
            errors.append(f"queue entries are not approved tasks: {', '.join(stale)}")

    for task_id, (version, path) in approved.items():
        queued_version = queued.get(task_id, (-1, path))[0]
        if queued_version != version:
            errors.append(
                f"{path}: queue has prompt version {queued_version}, recommendation has {version}"
            )

    if errors:
        print("Handoff validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Handoff validation passed for {len(approved)} approved task(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
