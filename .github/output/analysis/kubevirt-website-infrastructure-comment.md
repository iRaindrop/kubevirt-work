# Website and Infrastructure - Overall Comment

| Criterion | Rating (1-5) |
| --------- | ------------ |
| Single-source for all files | 2 - Needs improvement |
| Meets min website req. (for maturity level) | 3 - Meets standards |
| Usability, accessibility, and design | 3 - Meets standards |
| Branding and design | 4 - Meets or exceeds standards |
| Case studies/social proof | 3 - Meets standards |
| SEO, Analytics, and site-local search | 2 - Needs improvement |
| Maintenance planning | 3 - Meets standards |

Other Metrics:

| Criterion                                   | Rating (1-5) |
| ------------------------------------------- | ------------ |
| A11y plan & implementation                  | 3 - Meets standards |
| Mobile-first plan & implementation          | 3 - Meets standards |
| HTTPS access & HTTP redirect                | 4 - Meets or exceeds standards |
| Google Analytics 4 for production only      | 1 - Not present |
| Indexing allowed for production server only | 3 - Meets standards |
| Intra-site / local search                   | 4 - Meets or exceeds standards |
| Account custodians are documented           | 1 - Not present |

The KubeVirt web presence rests on a sound platform. MkDocs Material gives the user guide responsive layout, accessibility affordances, full-text search, and sitemaps for free; a Prow pipeline republishes both sites to GitHub Pages over HTTPS within a minute or two of merge; branding is applied once at the theme level; and the main website footer is a model of CNCF compliance. The project also has more adoption evidence than most incubating projects. The shortfalls are in measurement, connection, and stewardship rather than in the tooling.

Three themes recur across the areas:

- The user guide is invisible to the project. It carries no analytics, so nobody can see which pages are read, which searches fail, or which inbound links break. Nobody is documented as custodian of the analytics, Netlify, Search Console, DNS, or GitHub Pages accounts, the community `sig/documentation` entry has no members, and both repositories lean on one active documentation maintainer.
- The web properties do not act as one. Pages under `kubevirt.io` are built from three repositories with no documented content boundary, and user-facing content also sits in the core and CDI code repositories. The guide and the main site differ in generator, logo, typeface, header, and footer; neither search covers the other; and the guide links to none of the adopters, case studies, talks, or blog that make the project's case. The guide's footer also lacks the copyright, CNCF, and trademark elements the main site carries.
- Small defects touch every page. Header text fails WCAG AA contrast, `robots.txt` has a malformed sitemap URL, `netlify.toml` carries dead configuration, and production lacks an HSTS header. Each is a one-line fix.

The branding implementation, the automated publish pipeline, and the main website footer are strong enough to cite as examples for other projects.
