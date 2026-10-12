# KubeVirt beginner friendly issue backlog: answers

- Are docs issues well-triaged?

  Partially. The kubevirt/user-guide repository has a full Prow label set inherited from the KubeVirt organization: `kind/*`, `sig/*` (including `sig/documentation`), `triage/accepted`, `triage/needs-information`, `triage/duplicate`, and `lifecycle/*`. Org-level issue templates (`bug_report.md`, `docs_report.md`, `feature_request.md`) prompt reporters for structured information, and issues opened through them arrive with a consistent shape.

  The labels are applied inconsistently. Of the four issues open today, two carry a `kind/*` label and two carry no label at all; none has a `triage/*` or `sig/*` label and none is assigned. The two unlabeled issues are a proposal for Simplified Chinese documentation and a report that the Material theme is reaching end of life, both of which have been open for months without a maintainer response recorded in labels. Twelve issues were opened in the past year, so the volume is small enough that complete triage is achievable.

- Is there a clearly marked way for new contributors to make code or documentation contributions (i.e. a "good first issue" label)?

  Yes in form, no in substance. The repository defines both `good-first-issue` and `good first issue` labels and a `help wanted` label, and the Contributing page in the user guide tells newcomers to look for `good-first-issue` in the user-guide, kubevirt.github.io, and community repositories. The Contributing page also links a New Contributor session recording.

  There are currently zero open `good-first-issue` items in kubevirt/user-guide. In kubevirt/kubevirt, nine `good-first-issue` items are open and none is labeled `kind/documentation`, and no open kubevirt/kubevirt issue carries `kind/documentation` at all. A newcomer who follows the Contributing page's advice finds an empty list. Over the past year ten `good-first-issue` items were closed in kubevirt/user-guide, including a well-scoped batch of eight "Update ... Documentation to Reflect Feature Lifecycle Changes" issues (#918 through #925) filed in September 2025; all ten were closed by the stale bot with the `lifecycle/rotten` label rather than by a pull request.

- Are issues well-documented (i.e., more than just a title)?

  Yes. All four open issues have bodies over 300 characters. The enhancement issue #948 uses the feature request template, describes the problem (no clear structure for newcomers), and proposes persona-based getting-started paths. The closed `good-first-issue` batch was exemplary: each issue (for example #918) had a summary, a background section citing the specific kubevirt/kubevirt pull requests and versions that changed feature status, a list of affected files, and acceptance criteria, at roughly 1,800 characters.

  Issue quality is therefore not the constraint. The well-documented beginner issues expired unworked, which points to discoverability and follow-through rather than to how issues are written.

- Are issues maintained for staleness?

  Yes, mechanically. The KubeVirt Prow instance applies `lifecycle/stale` after inactivity, then `lifecycle/rotten`, then auto-closes, and `lifecycle/frozen` is available to exempt an issue. Of 21 issues closed in the past year, 15 (71 percent) were closed by this automation rather than by a fix. No open issue is older than about ten months and none has gone six months without an update, so the backlog does not accumulate.

  The same automation removed every beginner-friendly issue in the repository. The eight feature-lifecycle documentation issues were valid when filed and, as far as the closing comments show, were still valid when the bot closed them five months later; nobody applied `lifecycle/frozen` or `help wanted` to keep them alive. Staleness handling is tuned for a code repository with active triage and, without a human in the loop, it erases the entry points the Contributing page advertises.
