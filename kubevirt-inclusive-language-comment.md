# KubeVirt inclusive language: comment

The KubeVirt user guide is in good shape on inclusive naming. KubeVirt's own API objects, components, CLI, and feature gates avoid all Inclusive Naming Initiative tier-1 terms, the project's default branch is `main`, and the guide already uses "allowlist" where the older term might have appeared. The remaining occurrences of "master" are in URLs and third-party content, and the only one under the project's control, the 14 links to the API reference at the legacy `/master/` path, is a mechanical fix now that the API reference publishes under `/main/` and per-version paths. Field names such as `Abort Requested` are part of the KubeVirt API and are a question for the API maintainers rather than the documentation.

The one systemic concern is minimizing language. Words such as "simply", "simple", "easy", "easily", and "just" appear over a hundred times across 40 percent of pages. This language tells a reader who is struggling with a step that the step should have been easy, and in almost every case it can be deleted with no loss of meaning. Because the repository's spelling check has no rule for these words, the pattern will continue in new pages unless a style rule or lint check is added.

Strengths:

- No Inclusive Naming Initiative tier-1 terms in KubeVirt-controlled names, commands, or feature gates.
- "Allowlist" is used consistently for `permittedHostDevices`.
- No gendered pronouns or other exclusionary terms in prose.
- kubevirt.io home page is free of non-recommended terms.

Weaknesses:

- Over a hundred uses of "simple", "simply", "easy", "easily", and "just" across 39 pages.
- Fourteen API reference links still use the legacy `/api-reference/master/` path.
- A `kubevirt.io/nodeName: master` example remains on the Presets page.
- No style rule or automated check discourages minimizing language in new content.

Rating: 4 - Meets or exceeds standards
