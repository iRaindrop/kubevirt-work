# KubeVirt new contributor getting started content: comment

KubeVirt has a genuine new-contributor document and a mature community repository behind it. The user guide's Contributing page is written for someone making their first open source contribution: it sets expectations, points to low-barrier repositories, offers non-code ways to start, and links the governance, membership, code of conduct, and AI contribution policies. The kubevirt/community repository supplies the depth, including a SIG list, a membership checklist, a help-wanted label guide, and a detailed community meeting document, and both sides point at each other as the canonical entry.

The weakness is the hand-off from motivation to action. The Contributing page ends where a newcomer needs the most guidance: how to pick and claim an issue, how to fork, sign off, and open a pull request, what the Prow labels mean, and who will review. Those mechanics exist but are scattered across the repository README, kubevirt/kubevirt CONTRIBUTING.md, and kubevirt/kubevirt `docs/getting-started.md`, none of which is presented as the next step. The page also directs newcomers to `good-first-issue` lists that are currently empty, and does not name a channel, person, or meeting where a stuck contributor can ask for help. The community repository's most useful contributor resources (SIG list, help-wanted guide, meeting document, MAINTAINERS) are not linked from the guide at all.

Strengths:

- A dedicated, welcoming Contributing page that is the canonical entry point from both CONTRIBUTING.md and kubevirt/community.
- Explicit low-barrier starting points (documentation, website, community repositories) and non-code ways to contribute.
- A New Contributor session recording on YouTube.
- A comprehensive kubevirt/community repository with governance, membership, SIG, and meeting documentation.
- Community page and Welcome page surface the primary help channels.

Weaknesses:

- The Contributing page omits the contribution mechanics (claiming an issue, fork and PR flow, DCO, Prow labels, review expectations).
- Newcomers are sent to `good-first-issue` lists that are empty.
- No contributor-specific help guidance: which Slack channel to ask in, who reviews documentation, whether mentoring is available.
- The SIG list, help-wanted guide, community meeting document, and MAINTAINERS file in kubevirt/community are not linked from the guide.
- Build and test instructions for the guide live only in the repository README, not on the Contributing page.

Rating: 3 - Meets standards
