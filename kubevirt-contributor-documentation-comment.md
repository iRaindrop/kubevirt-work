# Contributor Documentation - Overall Comment

| Criterion | Rating (1-5) |
| --------- | ------------ |
| Communication methods documented | 4 - Meets or exceeds standards |
| Beginner friendly issue backlog | 2 - Needs improvement |
| "New contributor" getting started content | 3 - Meets standards |
| Project governance documentation | 4 - Meets or exceeds standards |

KubeVirt's contributor documentation is strong at the community level and thin at the point of use. The kubevirt/community repository holds mature governance, membership, SIG, and meeting documentation, the communication channels are active and well described, and the user guide has a welcoming Contributing page that is the canonical entry point. Two of the four areas exceed the standard for an incubating project. The one area that falls short, the beginner issue backlog, is the one a newcomer hits first when trying to act on that welcome.

Two themes recur across the areas:

- The good material is not surfaced where contributors and users are. Governance, maintainers, the SIG list, the help-wanted guide, and the community meeting details all live in the community repository and are barely linked from kubevirt.io or the user guide. The guide's header and footer carry no repository or chat icons, and its only help section is three bare URLs on the Welcome page.
- The path from invitation to first contribution breaks. The Contributing page motivates newcomers and then stops before the mechanics of claiming an issue, opening a pull request, and getting a review. It sends them to `good-first-issue` lists that are empty because every beginner issue from the past year was auto-closed by the stale bot rather than fixed or exempted. Nothing names a channel or person a stuck contributor can ask.

The governance documentation and the September 2025 batch of scoped, self-contained beginner issues are both good enough to cite as models for other projects; the backlog problem is one of triage follow-through, not of knowing how to write the issues.
