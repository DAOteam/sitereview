# BGRemove execution attempts

BGRemove uses `delivery_method: "direct_publish"`. Before changing production code, the programming AI creates a versioned attempt receipt named `<TASK-ID>-v<VERSION>-attempt-<NN>.md` from `templates/execution-result.md`.

`<NN>` is the next unused two-digit attempt number for that task and prompt version. The programming AI adds the receipt to the table when claiming the attempt and updates the same row when the attempt finishes.

Receipts record prompt-version handshake, stable item results, checks, publication, and production smoke tests. They are non-authoritative diagnostic evidence: implementation is still verified only by independently comparing each approved recommendation with the current production site.

| Task ID | Prompt version | Attempt | Status | Receipt | Updated |
|---|---:|---:|---|---|---|
