#!/usr/bin/env python3
"""Show the reusable cross-site daily execution and verification dashboard."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from validate_handoffs import ROOT, active_scope, frontmatter, queue_entries


PRIORITY = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


@dataclass
class QueueItem:
    site_id: str
    task_id: str
    version: int
    priority: str
    created_at: str
    state: str
    receipt: str = "-"


def recommendation_map() -> dict[str, tuple[dict[str, str], Path, str]]:
    records: dict[str, tuple[dict[str, str], Path, str]] = {}
    for path in ROOT.glob("sites/*/recommendations/*.md"):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        task_id = meta.get("task_id")
        if task_id:
            records[task_id] = (meta, path, text)
    return records


def receipt_item_results(text: str) -> dict[str, str]:
    return {
        item_id: result
        for item_id, result in re.findall(
            r"\|\s*`([A-Z]{2,4}-\d{4}-[A-Z0-9]+)`\s*\|\s*`(pass|fail|not_tested)`\s*\|",
            text,
        )
    }


def latest_receipt(
    site_dir: Path, task_id: str, version: int
) -> tuple[dict[str, str], Path, str] | None:
    candidates: list[tuple[int, dict[str, str], Path, str]] = []
    pattern = re.compile(
        rf"^{re.escape(task_id)}-v{version}-attempt-(\d{{2}})\.md$"
    )
    for path in (site_dir / "results").glob(f"{task_id}-v{version}-attempt-*.md"):
        match = pattern.match(path.name)
        if not match:
            continue
        text = path.read_text(encoding="utf-8")
        candidates.append((int(match.group(1)), frontmatter(text), path, text))
    if not candidates:
        return None
    _, meta, path, text = max(candidates, key=lambda item: item[0])
    return meta, path, text


def classify(
    site_dir: Path, task_id: str, version: int, recommendation_text: str
) -> tuple[str, str]:
    receipt = latest_receipt(site_dir, task_id, version)
    if receipt is None:
        return "execute", "-"

    meta, path, text = receipt
    status = meta.get("status", "unknown")
    if status == "in_progress":
        return "wait_in_progress", path.name
    if status == "blocked":
        return "resolve_blocker", path.name
    if status == "partial":
        return "review_partial", path.name
    if status != "published":
        return "review_invalid_receipt", path.name

    scope = active_scope(recommendation_text) or ""
    required_ids = set(re.findall(rf"{re.escape(task_id)}-[A-Z0-9]+", scope))
    results = receipt_item_results(text)
    if required_ids and all(results.get(item_id) == "pass" for item_id in required_ids):
        return "verify_online", path.name
    return "review_partial", path.name


def main() -> int:
    recommendations = recommendation_map()
    queue_items: list[QueueItem] = []
    errors: list[str] = []

    for index_path in sorted(ROOT.glob("sites/*/recommendations/index.md")):
        site_dir = index_path.parent.parent
        site_id = site_dir.name
        entries = queue_entries(index_path.read_text(encoding="utf-8"))
        for task_id, version in entries:
            record = recommendations.get(task_id)
            if record is None:
                errors.append(f"{site_id}: queued recommendation {task_id} is missing")
                continue
            meta, _, text = record
            state, receipt = classify(site_dir, task_id, version, text)
            queue_items.append(
                QueueItem(
                    site_id=site_id,
                    task_id=task_id,
                    version=version,
                    priority=meta.get("priority", "P9"),
                    created_at=meta.get("created_at", "9999-99-99"),
                    state=state,
                    receipt=receipt,
                )
            )

    if errors:
        print("Daily queue is invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Daily operations dashboard")
    if not queue_items:
        print("No approved tasks are queued.")
        return 0

    heads: list[QueueItem] = []
    seen_sites: set[str] = set()
    for item in queue_items:
        is_head = item.site_id not in seen_sites
        if is_head:
            heads.append(item)
            seen_sites.add(item.site_id)
        display_state = item.state if is_head else "queued_behind_head"
        print(
            f"- {item.site_id}: {item.task_id} v{item.version} "
            f"[{item.priority}] {display_state} receipt={item.receipt}"
        )

    executable = [item for item in heads if item.state == "execute"]
    candidate: QueueItem | None = None
    if executable:
        candidate = min(
            executable,
            key=lambda item: (
                PRIORITY.get(item.priority, 9),
                item.created_at,
                item.task_id,
            ),
        )
        print(
            f"Global execution candidate: {candidate.site_id} "
            f"{candidate.task_id} v{candidate.version}"
        )
    else:
        print("Global execution candidate: none")

    attention = [item for item in heads if item.state != "execute"]
    if attention:
        print("Attention before execution:")
        for item in attention:
            print(f"- {item.site_id}: {item.task_id} {item.state}")
        first = attention[0]
        print(
            f"Recommendation AI next action: reconcile {first.site_id} "
            f"{first.task_id} ({first.state})"
        )
    else:
        print("Recommendation AI next action: lightweight_monitoring")

    if candidate is None:
        print("Code execution AI next action: no_executable_task")
    else:
        print(
            f"Code execution AI next action: execute {candidate.site_id} "
            f"{candidate.task_id} v{candidate.version}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
