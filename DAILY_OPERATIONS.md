# Daily website operations

This runbook defines asynchronous AI-to-AI collaboration for every registered site. The recommendation/verification AI and code execution AI work independently. Humans do not relay task instructions, execution summaries, or approval messages between them; the central recommendation repository is their only handoff channel.

## Shared state machine

Each site execution queue is processed from the head only:

| Queue-head state | Recommendation/verification AI | Code execution AI |
|---|---|---|
| `execute` | May perform normal monitoring; leaves approved scope intact | Claims and executes this task |
| `wait_in_progress` | Does not create a duplicate or rewrite active scope | Continues only its existing attempt; another run stops |
| `verify_online` | Independently verifies current production | Stops and waits; never advances within the site |
| `review_partial` | Diagnoses from the receipt, verifies production, refreshes unresolved scope | Stops; never retries until a new prompt version exists |
| `resolve_blocker` | Resolves or reports the blocker and updates the recommendation state | Stops; never bypasses the task |
| `review_invalid_receipt` | Repairs or reports the invalid handoff record | Stops |

A recommendation is executable only when it is `approved`, is at the site queue head, validates successfully, and its current prompt version is classified `execute`.

## Independent daily job A — Recommendation and verification

The site owner runs the recommendation/verification AI on their own schedule with this standing instruction:

```text
执行今日审查工作。独立同步中央建议仓库，运行交接校验和每日队列看板。根据看板处理待线上验收、partial、blocked、无效回执和陈旧队列；只以真实生产站作为验收依据。随后执行轻量网站变化检测，只深查变化、失败、到期或明确指定的页面，最多创建或刷新一个最高价值任务。维护建议状态、prompt version、范围指纹和执行队列，完成后提交并推送中央仓库。不要向编码 AI发送消息，也不要等待编码 AI回复。
```

The recommendation/verification AI must:

1. Fetch the latest central repository state without overwriting remote work.
2. Run `python3 scripts/validate_handoffs.py` and `python3 scripts/daily_queue.py`.
3. Process every site queue head that needs recommendation-side attention:
   - `verify_online`: read the receipt only for diagnosis, then independently inspect production and classify every stable item.
   - `review_partial`: inspect the receipt, verify production, and carry only unresolved scope into a new prompt version.
   - `resolve_blocker`: resolve approved factual/process issues or record the exact user decision required.
   - `wait_in_progress`: leave the task untouched unless the receipt is demonstrably stale under a separately defined timeout policy.
4. Perform lightweight availability and change detection. Deep-check at most three changed, failed, expired, or explicitly requested pages.
5. Create or refresh at most one highest-value growth task per run. Do not create work merely to keep a queue non-empty.
6. Use `needs_decision` for unresolved business rules. Only the site owner approves pricing, billing, legal, data, migration, localization, or product-behavior decisions.
7. Update recommendation indexes, queue order, prompt versions, stable item IDs, and scope fingerprints together.
8. Rerun both scripts, commit, and push the recommendation-repository changes. The push is the handoff to the code execution AI.

If no receipt needs attention and no meaningful site change exists, record a concise healthy/no-new-task result. The code execution AI can still execute an existing approved queue head independently.

## Independent daily job B — Code execution

The developer runs the code execution AI on their own schedule with this standing instruction:

```text
执行今日代码工作。独立同步中央建议仓库，运行交接校验和每日队列看板。只执行看板给出的一个全局执行候选；完成版本握手、领取回执、编码、检查、发布、生产冒烟和最终回执后提交并推送中央仓库。若没有可执行候选，正常结束。不要联系审查人员，不要要求人工转述任务，也不要越过任何站点的队首状态。
```

The code execution AI must:

1. Fetch the latest central repository state before selecting work.
2. Run `python3 scripts/validate_handoffs.py` and `python3 scripts/daily_queue.py`.
3. If no global execution candidate exists, stop successfully and report the dashboard reason to its own operator only.
4. Select only the dashboard's global candidate. Execute at most one task per run.
5. Perform the task/version/fingerprint/item-ID handshake and push an `in_progress` receipt before modifying production code.
6. Inspect the authorized production-connected code workspace, implement only the active scope, and run item-level checks.
7. Publish only when the site's `delivery_method` and approved prompt authorize it.
8. Perform the required production smoke checks and mark every item `pass`, `fail`, or `not_tested`.
9. Update the attempt to `published`, `partial`, or `blocked`, update `results/index.md`, commit, and push the receipt. The push is the handoff to the recommendation/verification AI.
10. Do not change recommendation files or status, do not execute a second task, and do not wait for a human acknowledgement.

## Scheduling and ordering

The two jobs do not require direct coordination or a fixed order:

- If recommendation/verification runs first, it cleans verification and queue state before code execution sees it.
- If code execution runs first and the queue head is executable, it performs one task and leaves a receipt.
- If code execution sees `verify_online`, `review_partial`, `resolve_blocker`, or `wait_in_progress`, it exits safely without advancing the site.
- The next recommendation/verification run consumes the receipt from the repository; no person needs to forward the coding AI's response.

For faster same-day throughput, schedule recommendation/verification before code execution and optionally schedule a second recommendation/verification run later. For the safest minimal routine, run each job once daily; a publication may be independently verified on the next day's review.

## Cross-site selection

- Each site is gated by its own queue head.
- Sites waiting for verification or blocker resolution do not prevent another ready site from executing.
- Among executable site heads, the dashboard chooses one by P0, P1, P2, P3, then `created_at`, then `task_id`.
- There is at most one global code execution per daily code run.

## Safety and evidence boundaries

- The central repository is the only inter-agent handoff channel.
- Humans do not relay task bodies, prompt versions, execution summaries, or completion claims between agents.
- Execution receipts explain what the code execution AI attempted; they never verify production.
- Only the recommendation/verification AI may update recommendation status, and only current production evidence may produce `verified`.
- Neither AI force-pushes or overwrites unknown remote work. A sync conflict stops the run until the latest state is reconciled.
- Do not store credentials, customer data, cookies, signed-in identities, or environment values in recommendations or receipts.
