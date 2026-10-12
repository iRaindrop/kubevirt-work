# Single-Source Requirement - Comment

KubeVirt does not meet the single-source requirement as the CNCF criteria define it. The pages a visitor sees under `kubevirt.io` are built from three separate repositories with three separate publish pipelines, and user-facing documentation is additionally scattered across the `docs/` directories of the core and CDI code repositories. The split between the website and the user guide is defensible, since the two use different generators and serve different audiences, but that rationale is undocumented, and the overlap between `kubevirt/kubevirt/docs` and the user guide is not a design decision so much as an accumulation. Contributors have no written guidance on which repository a new page belongs in, and readers can land on developer-oriented Markdown in the core repository that duplicates or contradicts the user guide.

The user guide itself is a well-behaved single source: one `docs/` tree, explicit navigation files, and a redirect map for moved pages. That makes it the natural home for consolidating user-facing content that currently lives elsewhere, and the existing cross-links from the guide to `kubevirt/kubevirt/docs` and to the CDI repository identify exactly which content is a candidate to move.

Strengths:

- The user guide keeps all of its content in one `docs/` tree with declarative navigation and redirects.
- Each repository has one clear publish path, so there is no duplicate deployment of the same content.
- The website's docs page defers to the user guide rather than hosting a parallel copy.

Weaknesses:

- Website, user guide, and API reference are three repositories with no submodule or other mechanism tying them together.
- The `kubevirt/kubevirt/docs` directory holds about sixty files that overlap with user guide topics, and the guide links into it for getting-started content.
- CDI documentation lives in the CDI repository, and the guide links to it from six pages.
- No README or contributing guide explains which content belongs in which repository, or why the split exists.

Rating: 2 - Needs improvement
