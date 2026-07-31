# Recommendation repository agent rules

This repository is the source of truth for website recommendations and execution handoffs. It does not contain website source code.

## Roles

- The recommendation AI creates and updates files under `sites/*/recommendations/`.
- The code execution AI reads approved recommendations, modifies the separate target code repository, and writes a new file under `sites/*/results/`.
- The verification AI reviews implementation evidence and updates recommendation status.

## Execution gate

Only execute a recommendation when all conditions are true:

1. Its YAML frontmatter contains exactly `status: "approved"`.
2. The matching `site.md` contains a real `target_repository` and `default_branch`.
3. `Final decision`, `Implementation prompt`, and `Acceptance criteria` are complete.
4. No result file already claims the same task as `in_progress`.
5. The execution method matches `delivery_method`; when it is `pull_request`, never commit directly to the default branch.

Never execute `draft`, `needs_decision`, `deferred`, `blocked`, `rejected`, or `superseded` tasks.

## Execution protocol

1. Create `sites/<site-id>/results/<TASK-ID>-result.md` from the result template before changing code.
2. Work only in the target website code repository and within the approved prompt scope.
3. Do not deploy, publish, change billing products, or expose secrets unless the approved task explicitly authorizes that action.
4. When `delivery_method` is `pull_request`, create a task branch and open a Pull Request instead of pushing directly to the default branch.
5. Record the code branch, commit or PR, files changed, checks, blockers, and manual actions in the result file.
6. Do not edit the approved recommendation or mark it verified.

## Safety

- Never store credentials, payment secrets, environment variable values, or customer data here.
- Never invent repository URLs, product IDs, API contracts, analytics, rankings, or business decisions.
- Stop with a blocked result when required information is missing.
