# KubeVirt content maintainability: comment

The KubeVirt user guide is maintainable as a single-version, single-language site. Its toolchain is simple and well suited to a documentation-only repository: plain Markdown under `docs/`, mkdocs-material with built-in search, explicit `.nav.yml` ordering, centralized redirects, and a Makefile that runs spelling and link checks in a container. The redirects map shows the maintainers preserved URLs through a major reorganization, which is the kind of discipline that keeps a site maintainable over time.

The gap is that the project has outgrown the single-version model without documenting the alternative. KubeVirt ships minor releases with feature-gate graduations and API changes, and the repository already has per-release branches, yet the published site tracks only `main`, offers no version selector, and no document explains what the release branches are for or how contributors should use them. Users of an older KubeVirt cannot tell which features on a page apply to them except where an individual author added an "as of vX.Y" banner. Compared with the Kubernetes documentation that the CNCF criteria cite as a good example, which publishes each supported minor version with a selector and documents its branching and localization processes, KubeVirt's approach is informal and depends on maintainer memory.

Localization is absent but not blocked. There is no demand documented, no framework configured, and no language directory, so this is a low priority; the main cost of the current layout is that adding a first translation later would require moving every file.

Strengths:

- Simple, low-dependency MkDocs toolchain with search enabled on every page.
- Custom search separator tuned for hyphenated and dotted Kubernetes identifiers.
- Explicit `.nav.yml` ordering and a centralized redirects map preserve URLs across reorganizations.
- Makefile targets for local build, spell check, and link check.
- Release branches exist for recent minors, providing a foundation for versioned publishing.

Weaknesses:

- No published version selector; the live site tracks `main` only.
- No document describes the purpose, lifecycle, or publication status of the `release-vX.Y-*` branches, or when to cherry-pick.
- Version applicability is signaled inconsistently through ad hoc "as of vX.Y" banners on a minority of pages.
- No localization framework, language directory, or stated position on translation.
- Search does not span the API reference, quickstarts, or labs hosted elsewhere on kubevirt.io.

Rating: 3 - Meets standards
