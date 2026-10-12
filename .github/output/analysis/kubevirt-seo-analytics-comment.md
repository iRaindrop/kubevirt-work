# SEO Analytics and Site Search - Comment

The KubeVirt web presence splits across two sites with very different analytics postures. The main site collects data through a Red Hat–administered Adobe Analytics tag, while the user guide, which is the documentation users spend most of their time in, collects nothing. As a result the project has no visibility into which documentation pages are read, which searches fail, or which inbound links break. The main site's tag is also loaded on every deploy, so preview traffic is mixed into production numbers.

Search-engine fundamentals are in reasonable shape. Both sites produce sitemaps, the user guide emits correct canonical URLs even on its Netlify alias, and Google Search Console is verified for the domain. Local search works well in the user guide thanks to the MkDocs Material plugin, though the main site's lunr search indexes only blog posts and neither site can search the other. The biggest governance gap is that nobody is named as custodian of the analytics, Netlify, or Search Console accounts, and the project's dependence on a vendor-hosted analytics account is undocumented.

Strengths:

- Full-text local search in the user guide, with a tuned separator for technical tokens.
- Sitemaps for both sites and correct canonical links on user-guide pages.
- Google Search Console verification on the production domain.
- Proper HTTP 404 responses and custom not-found pages on both sites.

Weaknesses:

- No analytics on the user guide, so page-level usage and 404 data for documentation are unavailable.
- Main-site analytics run on previews and local builds as well as production.
- Main-site search indexes blog posts only, and there is no cross-site search.
- The `robots.txt` on kubevirt.io references a malformed sitemap URL and omits the user-guide sitemap.
- Custodians of the analytics, Netlify, and Search Console accounts are not documented.

Rating: 2 - Needs improvement
