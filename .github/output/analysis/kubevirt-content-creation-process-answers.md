# KubeVirt content creation process: answers

- Is there a clearly documented (ongoing) contribution process for documentation?

  Partially. The repository README documents the mechanics: fork, edit Markdown under `docs/`, keep `.nav.yml` ordering current, sign commits with `-s`, run `make build_img`, `make check_spelling`, `make check_links`, and `make run` in a container, then open a pull request. The root CONTRIBUTING.md is a two-line pointer to the Contributing page on the published site, and that page covers community-wide onboarding (prerequisites, where to find good-first-issues, the Code of Conduct, membership policy, governance, and the AI contribution policy) with the user guide listed as a low-barrier repository.

  The process stops at "open a PR". Nothing in the repository describes what happens next: which labels are applied, who is expected to review, what the approval flow is, how long a contributor should expect to wait, or when to use the release branches. There is no documentation style guide, page template, or guidance on when a change needs a redirect entry in `mkdocs.yml`. The repository has no pull request or issue templates under `.github/`. Twelve pull requests are open, the oldest from March 2026.

- Does the code release process account for documentation creation & updates?

  Yes. The kubevirt/kubevirt pull request template includes a checklist item that a user-guide update "was considered and is present (link) or not required" for any user-facing feature or API change, and approvers are asked to review the list. The Virtualization Enhancement Proposal (VEP) process in kubevirt/enhancements requires SIGs, after code freeze, to confirm that the "Docs PR is merged (plan review ahead of release if only placeholder is opened)" as part of the release tracking checklist.

  The process is visible in practice. Recent merged pull requests include VEP 190 plugins documentation, GPU DRA, Migration Stall Detector alpha docs, PersistentReservation GA graduation, Template Beta graduation, and the v1.9.0 release notes, most authored by the feature developers themselves. Release notes are regenerated from kubevirt/kubevirt tags with `update_changelog.sh`. Neither the PR checklist item nor the VEP requirement is enforced by tooling, and the user guide repository itself does not document how its `release-vX.Y-*` branches relate to the KubeVirt release cycle.

- Who reviews and approves documentation pull requests?

  Prow, using the `OWNERS` and `OWNERS_ALIASES` files. The root `OWNERS` file assigns every path to the `reviewers` alias (seven people) and the `approvers` alias (ten people), and automatically labels changes under `docs/` with `kind/documentation`. `OWNERS_ALIASES` also defines per-SIG reviewer and approver groups for network, storage, compute, observability, release, test, scale, and buildsystem, but the `OWNERS` file does not route any directory to them, so SIG experts are not auto-assigned to pages in their area. Presubmit and postsubmit Prow jobs for the repository are defined in kubevirt/project-infra.

  The reviewer and approver lists are made up of KubeVirt core maintainers rather than documentation specialists, and one contributor (aburdenthehand) is the most frequent committer over the last six months and authored the v1.9.0 release notes and site fixes. The process is discoverable only by reading the `OWNERS` files; no human-readable page names the documentation approvers or explains the Prow `/lgtm` and `/approve` flow to a first-time contributor.

- Does the website have a clear owner/maintainer?

  Partially. The user guide is owned collectively by the `approvers` alias in `OWNERS_ALIASES`, the site builds on Netlify from `main` (badge in the README, configuration in `netlify.toml`), and the `OWNERS` file labels changes under `site/` with `kind/website`. Seven emeritus approvers are listed, showing the list is curated over time. The main website, kubevirt.io, is a separate repository (kubevirt/kubevirt.github.io) with its own ownership.

  There is no MAINTAINERS file, no named documentation lead or SIG Docs, and no statement on the Contributing page or README of who is responsible for the user guide's infrastructure, the Netlify account, or the release-notes process. Ownership is inferable from Git history and OWNERS files but is not documented.
