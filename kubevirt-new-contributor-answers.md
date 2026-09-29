# KubeVirt new contributor getting started content: answers

- Do you have a community repository or section on your website?

  Yes, both. The kubevirt/community repository holds the governance document, membership policy and checklist, maintainers and alumni lists, code of conduct, AI contribution policy, community meeting mechanics, a SIG list with per-SIG charters, working groups, a help-wanted label guide adapted from Kubernetes, and directories for events, design proposals, and conference proposals. The kubevirt.io website has a Community page with the shared calendar, GitHub, Slack, mailing list, and YouTube links, and a Contributing tab in the user guide's top navigation.

  The two are loosely connected. The kubevirt/community `contributors/contributing.md` is a one-line pointer to the user guide's Contributing page, and the user guide's Contributing page links back to the membership policy, governance, code of conduct, and AI policy in kubevirt/community. However, the Contributing page does not link the community repository's SIG list, help-wanted guide, community meeting document, or MAINTAINERS file, so a newcomer sees only part of what the community repository offers.

- Is there a document specifically for new contributors/your first contribution?

  Yes. The user guide's Contributing page is written for first-time contributors and is the canonical entry point that both the root CONTRIBUTING.md and kubevirt/community point to. It has a Prerequisites section (CNCF open source primer, Git basics, the organization's repositories, quick start labs), a "Your first contribution" section that lists documentation and community repositories as low-barrier starting points and code repositories for Go developers, an "Other ways to get started" section (review a pull request, watch the New Contributor session recording, open an issue), and links to the community's core documents.

  The document stops before the mechanics. It tells readers to look for `good-first-issue` but the linked repositories currently have no such open issues, and it does not describe how to claim an issue, the fork-branch-PR flow with DCO sign-off, what Prow labels and `/lgtm` and `/approve` mean, or how long review takes. Those mechanics are split between the repository README (build, spell check, link check, sign-off) for documentation and kubevirt/kubevirt's CONTRIBUTING.md and `docs/getting-started.md` for code. The kubevirt/kubevirt CONTRIBUTING.md is the more complete document, covering workflow, testing, draft pull requests, DCO, review, and membership, but it is written for code contributors and is not surfaced in the user guide beyond one link.

- Do new users know where to get help?

  Partially. The Welcome page's "Getting help" section lists the GitHub issue tracker, the kubevirt-dev mailing list, and the `#virtualization` Slack channel. The Contributing page invites readers to raise a bug if something is missing, points to the Community page, and links the New Contributor session recording. The kubevirt/community help-wanted guide states that `good first issue` items come with a commitment from members to provide extra assistance.

  Help is not framed for contributors specifically. Nothing tells a new contributor which Slack channel to ask in when stuck on a documentation pull request (`#kubevirt-dev` is not named in the guide), who the documentation approvers are, whether there is a mentor or buddy program, or that the weekly community meeting welcomes newcomer introductions. The help links are bare URLs on the Welcome page and are not repeated on the Contributing page or in CONTRIBUTING.md.
