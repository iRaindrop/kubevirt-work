# Maintenance Planning - Recommendations

The following recommendations address the maintenance planning of the KubeVirt user guide.

- Document infrastructure ownership. Add a "Site infrastructure" section to the README of both `kubevirt/user-guide` and `kubevirt/kubevirt.github.io` (or a page in `kubevirt/community`) that lists who administers the Netlify site, GitHub Pages and custom-domain settings, DNS for kubevirt.io, and the Prow job definitions in `kubevirt/project-infra`, and how a maintainer requests access.
- Give documentation a formal home. Populate the `sig/documentation` entry in the community `sig-list.md` with chairs, a meeting cadence or async channel, and a charter that includes both the user guide and the website, so newcomers know where to volunteer and maintainers have a succession path.
- Publish a maintainer ladder. In the website and user-guide READMEs, describe how a contributor becomes a reviewer and then an approver (for example, a number of merged docs PRs and a nomination), mirroring the process in `kubevirt/community` for code SIGs.
- Reduce bus-factor risk by recruiting at least one additional regular website reviewer for each repository, using the existing `kind/website` and `kind/documentation` labels and a `good-first-issue` pass to seed starter tasks.
- Plan to converge the two toolchains. Evaluate moving the main site to MkDocs Material or another Hugo/Docusaurus-style generator with a supported theme so a single skill set covers both sites, and track the decision in an issue even if the migration is deferred.
- Clean up `netlify.toml` in the user-guide repository: remove the obsolete `sed` line that targets `site_url: https://kubevirt.io/docs`, and pin the MkDocs package versions (or use a `requirements.txt`) so preview builds are reproducible and match the Prow image.
- Add a `Strict-Transport-Security` header. GitHub Pages does not let you set response headers directly, so either enable HSTS through the DNS/CDN provider in front of kubevirt.io or, if none exists, record the limitation in the infrastructure section so it is a known gap.
- Periodically review `OWNERS_ALIASES` in the user-guide repository and add dated emeritus entries as the website repository already does, so the approver list reflects who is actually active.
