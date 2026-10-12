# KubeVirt project governance documentation: comment

KubeVirt's governance documentation is clear, specific, and maintained. `GOVERNANCE.md` answers the questions an evaluator asks first: who the maintainers are, how they are chosen and removed, how votes work and what thresholds apply, and how SIGs and working groups relate to the maintainers. The companion documents give the contributor ladder concrete requirements at each level and an explicit inactivity policy, the maintainers list records employers and areas of responsibility with an emeritus table, and SIG charters are generated from a single source of truth. This is the level of governance documentation expected of a CNCF incubating project and is a strength the project can point to.

The only shortfall is presentation. Governance is documented in the community repository but not summarized or prominently linked from kubevirt.io or the user guide; the Contributing page links `GOVERNANCE.md` with a one-line label among other resources, and the Community page does not mention governance, maintainers, or SIGs at all. Prospective adopters and contributors evaluating the project from the website have to know the community repository exists to find this material.

Strengths:

- `GOVERNANCE.md` covers maintainer selection, removal, voting thresholds, meetings, SIGs, subprojects, and working groups with concrete rules.
- `MAINTAINERS.md` lists current maintainers with employer and responsibilities plus an emeritus table, and is tied to the CNCF maintainers list.
- `membership_policy.md` defines a full contributor ladder with requirements, privileges, and a measurable inactivity policy.
- SIGs and working groups are declared in `sigs.yaml` and the SIG list is generated, so it cannot drift from the source.
- Code of conduct, AI contribution policy, and CNCF incubation records are co-located.

Weaknesses:

- The kubevirt.io Community page does not link governance, maintainers, or the SIG list.
- The user guide's Contributing page links `GOVERNANCE.md` with a one-line label and no summary.
- Neither site names the maintainers or explains how decisions are made.

Rating: 4 - Meets or exceeds standards
