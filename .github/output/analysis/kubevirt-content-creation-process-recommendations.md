# KubeVirt content creation process: recommendations

The following recommendations address the content creation process of the KubeVirt user guide.

- Expand CONTRIBUTING.md from a pointer into a documentation contributor guide that covers the full lifecycle: how to propose a change, how to build and test locally (move the README build steps here), what happens after opening a PR (labels, `/lgtm`, `/approve`, expected turnaround), when to add a redirect to `mkdocs.yml`, and when a change needs a cherry-pick to a `release-vX.Y-stable` branch. Model it on the Thanos "How to contribute to docs" page.
- Add a MAINTAINERS.md (or a "Maintainers" section on the Contributing page) that names the user guide approvers, the person or group responsible for the Netlify deployment and the release-notes script, and how to reach them. Model it on the NATS site MAINTAINERS file.
- Add a short documentation style guide covering page structure (title, short concept, feature-state banner, procedure, related links), the standard feature-state admonition, code block conventions (fenced blocks, no `$` prompts), Kubernetes object capitalization, and file naming. Link it from CONTRIBUTING.md and the Contributing page.
- Add a pull request template to `.github/` with a checklist: `.nav.yml` updated for new pages, redirect added for moved pages, spelling and link checks run, feature-state banner present, and the related kubevirt/kubevirt PR or VEP linked.
- Route reviews to subject-matter experts by adding per-directory `OWNERS` files (for example `docs/network/OWNERS`, `docs/storage/OWNERS`, `docs/compute/OWNERS`) that reference the existing `sig-network-*`, `sig-storage-*`, and `sig-compute-*` aliases, while keeping the root approvers for site-wide changes.
- Ask the maintainers to consider a documentation-focused reviewer role or SIG Docs alias, so that writers who are not core code approvers can share the review load and reduce the open PR backlog.
- Document the release-cycle touchpoints for the user guide on the Contributing page: when a release branch is cut, that the VEP checklist requires the docs PR to be merged by code freeze, and how the release notes page is regenerated with `update_changelog.sh`.
- Triage the twelve open pull requests, closing or merging the oldest, and add a stale-PR policy to CONTRIBUTING.md so contributors know what to expect.
