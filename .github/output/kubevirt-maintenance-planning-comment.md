# Maintenance Planning - Comment

The KubeVirt documentation infrastructure is low-maintenance by design and largely automated. The user guide runs on MkDocs Material, one of the most widely adopted documentation stacks in the cloud-native ecosystem, and both sites are published to GitHub Pages by a Prow job within a minute or two of merge. HTTPS is enforced everywhere, Netlify provides pull-request previews, and Dependabot keeps the Jekyll site's dependencies current. For a project of KubeVirt's size, the tooling choices are sensible and the deploy pipeline is fast and hands-off.

The risk lies in people rather than tooling. The two sites use different generators, so a maintainer must know both Jekyll and MkDocs, and the main site's hand-built Bootstrap theme has no upstream to inherit fixes from. Commit history shows the documentation effort leaning on a single active maintainer, the community's `sig/documentation` label has no chairs or members, and neither repository describes how someone grows into a website maintainer role or who holds the keys to Netlify, DNS, GitHub Pages settings, and the Prow job definitions. If that maintainer stepped away, the project would have working automation but no documented map of who can change it.

Strengths:

- MkDocs Material for the user guide is well supported and common among CNCF projects.
- Fully automated publish pipeline: merge to `main` triggers a Prow job that pushes to `gh-pages` in roughly 40 to 90 seconds.
- HTTPS everywhere, with HTTP and `www` redirecting to the canonical HTTPS domain.
- `OWNERS` files are maintained, including dated emeritus entries on the website repository.
- Netlify pull-request previews and a periodic Prow link checker catch problems before and after publish.

Weaknesses:

- Two different static-site generators and a custom Jekyll theme double the maintenance surface.
- No documented path for cultivating website maintainers; the `sig/documentation` entry in the community SIG list is empty.
- Heavy reliance on one active documentation maintainer across both repositories.
- Administrative access to Netlify, DNS, GitHub Pages, and Prow job definitions is undocumented.
- No `Strict-Transport-Security` header on production responses.

Rating: 3 - Meets standards
