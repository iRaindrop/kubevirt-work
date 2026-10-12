# KubeVirt content maintainability: answers

- Is the documentation searchable?

  Yes. The site uses the built-in MkDocs search plugin with the mkdocs-material theme, so a search box appears in the header on every page and results are served from a client-side index built at deploy time. `mkdocs.yml` sets a custom separator that splits on punctuation such as hyphens, colons, and slashes while preserving version numbers like `v1.9.0`, which helps with Kubernetes-style identifiers such as `kubevirt.io/libvirt-log-filters` and `virt-handler`.

  Search is confined to the user guide. The API reference at kubevirt.io/api-reference, the quickstarts and labs on kubevirt.io, and the release notes in the kubevirt/kubevirt repository are separate sites with their own or no search, so a user cannot search across the KubeVirt documentation set from one box. The theme's search enhancements (`search.suggest`, `search.highlight`, `search.share`) are not enabled.

- Are there plans for localization/internationalization with regards to site directory structure? Is a localization framework present?

  No. All content is English and lives directly under `docs/`, with no language-code directory such as `docs/en/`. `mkdocs.yml` does not configure the mkdocs-material `alternate` language selector or the `i18n` plugin, and neither README nor CONTRIBUTING mentions translation. No open plans for localization are documented in the repository.

  The directory layout does not block a future effort. Content is plain Markdown organized by section, ordering is controlled by `.nav.yml` files, and redirects are centralized in `mkdocs.yml`, so a language-prefixed tree could be introduced later. The absence of a root language directory means that step would require moving every file and updating every redirect.

- Is there a clearly documented method for versioning of content?

  No. The published site at kubevirt.io/user-guide is built from the `main` branch by Netlify and has no version selector; the only version indicators are a v1.9.0 release notes page and in-text "as of vX.Y" feature-state banners on about ten pages. `mkdocs.yml` has no `extra.version` configuration and the `mike` versioning tool is not used.

  The repository does contain release branches (`release-v1.7-stable`, `release-v1.8-stable`, `release-v1.9-stable`, and matching `-devel` branches for 1.7 and 1.8), and they have received commits, so a branching convention exists in practice. However, no document in the repository explains what those branches are for, whether they are published anywhere, how or when they are cut, or how contributors should decide whether a change needs a cherry-pick. README, CONTRIBUTING, and the Contributing page all describe the fork-and-PR flow against `main` only. Release notes are maintained by a script (`update_changelog.sh`) that regenerates the page from kubevirt/kubevirt tags, but that process is also undocumented outside the script itself.
