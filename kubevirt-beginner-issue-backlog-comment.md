# KubeVirt beginner friendly issue backlog: comment

The KubeVirt user guide has the infrastructure for a beginner-friendly backlog but not the backlog itself. The repository inherits the KubeVirt organization's Prow labels, issue templates, and lifecycle automation; the labels a newcomer needs (`good-first-issue`, `help wanted`, `sig/documentation`, `triage/accepted`) all exist; and the Contributing page points newcomers at `good-first-issue` in this and two sibling repositories. When maintainers have written beginner issues, they have written them well: the September 2025 batch of eight feature-lifecycle documentation issues each carried background, affected files, and acceptance criteria.

The problem is follow-through. All ten `good-first-issue` items closed in the past year, including that entire batch, were auto-closed by the stale bot without a fix, and today the label has zero open items here and zero documentation-related items in kubevirt/kubevirt. A newcomer who follows the Contributing page's instructions finds nothing to do. Triage labels are applied to only half of the small open backlog, and no issue is assigned or marked `triage/accepted`, so the lifecycle automation runs without a human deciding which issues should survive it. The net effect is a clean but empty backlog, which is the wrong outcome for a project that explicitly invites first-time contributors to start with documentation.

Strengths:

- Full Prow label taxonomy, org-level issue templates, and automated lifecycle management are in place.
- Open issues are substantive, with structured bodies and clear problem statements.
- The retired `good-first-issue` batch (#918 to #925) is a model for how to write scoped, self-contained documentation tasks.
- Issue volume (twelve per year) is small enough to triage completely.
- The Contributing page tells newcomers which label to look for and in which repositories.

Weaknesses:

- Zero open `good-first-issue` items in kubevirt/user-guide and zero documentation-labeled beginner issues in kubevirt/kubevirt.
- Every beginner issue closed in the past year was auto-closed as rotten rather than fixed.
- Half of open issues are unlabeled; none carries `triage/*`, `sig/*`, or an assignee.
- No process exempts valid, unworked beginner issues from the stale bot.
- A proposal for Simplified Chinese documentation and a theme end-of-life report have no recorded triage decision.

Rating: 2 - Needs improvement
