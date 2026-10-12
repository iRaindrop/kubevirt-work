---
mode: agent
description: Create GitHub issue files in .github/output/issues/ from the ranked KubeVirt analysis recommendations, bundling related recommendations into umbrella issues scoped to 2-4 hours each.
---

# Create documentation issues from the KubeVirt analysis recommendations

## Role and goal

You are a senior technical writer on the CNCF TechDocs team. Turn the ranked recommendations from the KubeVirt user guide documentation analysis into GitHub issue files that a technical writer or engineer with KubeVirt context can pick up and complete. A process will later upload every file in the output directory to GitHub, so each file must be a complete, uploadable issue.

## Sources

Use only these sources. Do not add issues from your general knowledge of the KubeVirt repositories or documentation; the assessment defines the scope.

- `.github/input/ai-ranked-recommendations.csv` — the ranked recommendations. Columns: `Section`, `Area`, `Recommendation`, `Suggested Priority` (`1 - Urgent`, `2 - High`, `3 - Backlog`).
- `.github/output/analysis/kubevirt-*-recommendations.md` — the per-area recommendations files, for context on why each recommendation was made.
- `.github/output/analysis/kubevirt-*-comment.md` — the per-area comments, only when you need the problem statement behind a recommendation.
- `.github/issue_template/kubevirt-doc-issue.md` — the template for a single issue.
- `.github/issue_template/umbrella-issue.md` — the template for an umbrella issue with sub-issues.
- https://github.com/cncf/techdocs/issues/221 — the CNCF TechDocs Assistance issues tracker. Read how previous analyses organized their issues and follow the same conventions for titles, scope, and tone.

## Procedure

1. Read the CSV and the recommendations files. Group the recommendations by section and area.
2. Decide which recommendations are issues. A recommendation is an issue when it describes a concrete problem or gap in the documentation that a contributor can fix. Skip recommendations that are optional improvements with minimal impact, that depend on decisions the maintainers have not made, or that cannot be acted on without information the assessment does not provide. Record every skipped recommendation and the reason in the coverage report (see Outputs).
3. Bundle related recommendations into umbrella issues. Group by theme, not strictly by area; a theme may span areas or sections. Each umbrella issue has three to ten sub-issues. Each sub-issue may bundle several small recommendations.
4. Scope every issue and sub-issue to about two to four hours of work for a technical writer or engineer with KubeVirt context. Split a recommendation that is larger than that; merge recommendations that are smaller.
5. Write a standalone issue for a recommendation that does not fit a theme but is still worth fixing on its own.
6. Assign a priority label to every file. Start from the CSV ranking without its number prefix (`1 - Urgent` → `urgent`, `2 - High` → `high`, `3 - Backlog` → `backlog`). You may adjust the priority when bundling changes the impact; an umbrella issue takes the highest priority of its sub-issues. Note any adjustment in the coverage report.
7. Keep the total number of issue files well below the number of recommendations. A good target is 10 to 20 files. If you exceed that, bundle further.

## Issue file format

Every file in `.github/output/issues/` starts with this front matter, followed by the issue body:

```yaml
---
title: <GitHub issue title>
labels: [<urgent | high | backlog>, help wanted]
repo: https://github.com/kubevirt/user-guide/issues
---
```

- `title` becomes the GitHub issue title. Make it specific and imperative, for example "Add a Getting Started page that walks through creating and starting a VirtualMachine".
- `labels` becomes the GitHub issue labels. Include exactly one of `urgent`, `high`, or `backlog`, and always include `help wanted`. Do not add any other labels.
- `repo` is always `https://github.com/kubevirt/user-guide/issues`.
- Everything after the front matter is the issue description. Write it in GitHub-flavored Markdown.

For a single issue, follow `kubevirt-doc-issue.md`: keep its `## Description`, `## What you expected`, `## URL`, and `## Additional context` headings. Under `## URL`, link to the affected pages on https://kubevirt.io/user-guide/ and name the Markdown files under `docs/`.

For an umbrella issue, follow `umbrella-issue.md`: write an `## Overview` that states the problem the theme addresses and how the sub-issues resolve it, then a `## Sub-issues` section with one `### <sub-issue title>` heading per sub-issue. Each sub-issue describes what to change, where (page titles and `docs/` paths), and what done looks like. Add headings or subheadings when they help organize the content.

In all issue bodies:

- Write in complete sentences, active voice, and the imperative mood.
- Explain any term a senior Kubernetes engineer might not know; do not explain Kubernetes basics.
- Follow Kubernetes documentation conventions: UpperCamelCase for API objects such as VirtualMachine and VirtualMachineInstance, and code formatting for commands, fields, and file names.
- If you are unsure whether something is technically wrong, phrase it as a question for the maintainers rather than asserting it.
- Do not mention the CSV, the priority ranking, or this prompt in the issue body. The body is for KubeVirt contributors.

## Outputs

1. Issue files in `.github/output/issues/`. Name each file after its title, lowercased, with hyphens between words and no punctuation, for example `add-getting-started-page.md`. Overwrite existing files with the same name.
2. A coverage report at `.github/output/issues-coverage.md` (outside the issues directory so it is not uploaded as an issue). Include:
   - A table mapping every CSV recommendation to the issue file and sub-issue that covers it, or "Not an issue" with a one-sentence reason.
   - A list of priority adjustments with the original ranking, the new label, and the reason.
   - A count of recommendations, issue files, and sub-issues.

When finished, summarize the issue files you created (title, label, number of sub-issues) and ask the writer to review the scope of each one.
