# Daily website operations

This runbook is the reusable operating loop for every registered site. It is not tied to a specific task ID or current backlog.

## Operating principle

One daily cycle may discover, execute, and verify work, but each role remains separate:

- The recommendation/verification AI observes public production, manages decisions, creates or refreshes recommendations, and owns recommendation status.
- The code execution AI implements exactly one approved task per run, publishes only when the site's delivery method authorizes it, and writes execution evidence.
- The user approves unresolved business decisions and initiates each role. Execution receipts never replace independent production verification.

## Phase 1 — Morning review

Run this in the recommendation/verification AI:

```text
执行今日网站运营。同步中央建议仓库，运行交接校验和每日队列看板。先处理所有待线上验收、partial、blocked 和陈旧队列，再做轻量变化检测。只深查变化、失败、到期或我指定的页面，最多生成一个主增长任务；未确认的业务规则不得自动批准。完成后提交并推送建议仓库更新。
```

The recommendation/verification AI must:

1. Sync the central repository without overwriting remote work.
2. Run `python3 scripts/validate_handoffs.py` and `python3 scripts/daily_queue.py`.
3. Reconcile queue-head receipts before proposing new execution for the same site:
   - `verify_online`: independently inspect current production and classify every stable item.
   - `review_partial`: inspect the receipt for diagnosis, then inspect production and refresh only unresolved scope.
   - `resolve_blocker`: report the exact blocker or decision needed.
   - `wait_in_progress`: do not create a duplicate attempt.
4. Perform lightweight availability and change detection. Deep-check at most three changed, failed, expired, or requested pages.
5. Create at most one highest-value new recommendation. Use `needs_decision` when user input is required; do not auto-approve it.
6. Update recommendation indexes, execution queues, prompt versions, stable item IDs, and scope fingerprints together.
7. Commit and push the recommendation-repository changes when the user has authorized the daily workflow to do so.

## Phase 2 — One code execution

Run this in the code execution AI after Phase 1 is clean:

```text
执行今日代码任务。按中央建议仓库的每日看板选择一个全局最高优先级任务；不要跳过任何站点的待验收、部分完成、阻塞或正在执行队首任务。
```

The code execution AI must:

1. Sync the central repository and run both dashboard commands.
2. If a site queue head needs verification, review, blocker resolution, or is already in progress, do not advance within that site.
3. Among executable site queue heads, choose one by priority, creation date, then task ID.
4. Perform the version handshake and create the next versioned attempt receipt before editing production code.
5. Implement, test, publish, and production-smoke-test only that task.
6. Mark every stable item `pass`, `fail`, or `not_tested`; required failures or untested states make the attempt `partial` or `blocked`.
7. Update and push the receipt. Do not change recommendation status.

If no task is executable, the correct output is a short dashboard with the verification, blocker, decision, or empty-queue reason. Do not invent work.

## Phase 3 — Post-publication verification

Run this in the recommendation/verification AI after the code execution AI reports `published` or `partial`:

```text
执行今日发布后验收。读取最新执行回执用于诊断，但只以当前公开生产站为最终依据。逐项验收稳定 item ID，更新状态、下一 prompt version 和执行队列，然后提交并推送建议仓库更新。
```

The recommendation/verification AI must:

1. Inspect the current public production URLs and any safely available authenticated state required by the task.
2. Classify each item as `verified_online`, `still_open`, `partially_applied`, or `no_longer_relevant`.
3. Mark the recommendation `verified` only when all required items pass independently.
4. Otherwise preserve stable item IDs, remove completed scope, increment `prompt_version`, recompute the scope fingerprint, and keep the task at the site queue head.
5. Rerun both dashboard commands and report the next daily action.

## Phase 4 — Daily close

The final daily report contains only:

- Production verifications completed today.
- The one code task executed today, if any.
- Partial attempts or blockers.
- Decisions required from the user.
- The next global executable candidate.
- Whether tomorrow should begin with verification, execution, review, or lightweight monitoring.

## Safety and stop conditions

- Do not execute more than one code task per daily code run.
- Do not stack multiple unverified publications on the same site.
- Do not auto-approve pricing, billing, legal, data, migration, localization, or product-behavior decisions.
- Do not use receipts, source code, commits, or branches as production verification.
- Do not retry `partial` or `blocked` attempts until the recommendation/verification AI has reconciled them.
- Do not create a task merely to keep the queue non-empty.
