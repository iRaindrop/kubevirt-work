# SEO Analytics and Site Search - Answers

- Is analytics enabled for the production server?

  Partially. The main website (kubevirt.io, built from the kubevirt.github.io repository) loads Adobe Analytics through a Red Hat–hosted tag script (`//www.redhat.com/ma/dpal.js`) in `_includes/head.html`, so page views on the main site are collected. The user guide (kubevirt.io/user-guide, built from this repository with MkDocs) has no analytics of any kind: `mkdocs.yml` contains no `extra.analytics` block, and the rendered pages load only the Material theme bundle. The main site also carries a `google-site-verification` meta tag, indicating that Google Search Console is set up for the domain.

- Is analytics disabled for all other deploys?

  No for the main site; not applicable for the user guide. The Adobe Analytics script is included unconditionally in the main site's `head.html`, with no check on the Jekyll environment or the Netlify deploy context, so it also runs on Netlify deploy previews and local builds. The user guide has no analytics in any deploy, including the Netlify production alias (`kubevirt-user-guide.netlify.app`) and pull-request previews.

- If project is using Google Analytics, has it migrated to GA4?

  Not applicable. The project uses Adobe Analytics rather than Google Analytics, so there is no Universal Analytics property to migrate. No `G-` or `UA-` measurement ID appears in either repository or in the rendered pages.

- Can Page-not-found (404) reports easily be generated from site analytics?

  Not for the user guide, because it has no analytics; broken inbound links to the user guide are invisible. Both sites do serve proper 404 responses (the user guide returns HTTP 404 with the Material theme's not-found page, and the main site has a custom `404.html`), so a 404 report would be possible if page-level analytics were collecting the URL. For the main site, whether a 404 report is available depends on the Adobe Analytics workspace that Red Hat administers, and nothing in the repositories documents how to obtain one.

- Is site indexing supported for the production server, while disabled for website previews and builds for non-default branches?

  Indexing is supported in production. The main site generates a sitemap with `jekyll-sitemap`, and MkDocs generates `https://kubevirt.io/user-guide/sitemap.xml`, which resolves with HTTP 200. Each user-guide page sets a canonical link to `https://kubevirt.io/user-guide/...` because `site_url` is set in `mkdocs.yml`, and the canonical is preserved on the Netlify alias, which steers search engines to the production URL. The `robots.txt` at kubevirt.io contains only a Sitemap directive (with a stray double slash, `https://kubevirt.io//sitemap.xml`) and does not reference the user guide sitemap. Neither repository sets a `noindex` meta tag or `X-Robots-Tag` header for previews; the project relies on Netlify's default behavior of marking deploy-preview URLs as `noindex`. The `netlify.toml` in this repository still runs a `sed` command that rewrites `site_url: https://kubevirt.io/docs`, a value that no longer exists in `mkdocs.yml`, so that step is a no-op.

- Is local intra-site search available from the website?

  Yes for the user guide, and only partially for the main site. The user guide enables the MkDocs Material `search` plugin with a custom token separator, and the search box appears in the header on every page. The main site has a `search.html` page backed by lunr.js, but its index is built only from `site.posts`, so it covers blog posts and not the main site's other pages. Neither search covers the other site; a user-guide search does not surface blog or main-site content, and the main-site search does not surface user-guide pages.

- Are the current custodian(s) of the analytics accounts (such as Google CSE) documented?

  No. Neither repository documents who administers the Adobe Analytics property, the Netlify sites (`kubevirt-user-guide` and the main site), or the Google Search Console verification. The `OWNERS` and `OWNERS_ALIASES` files list code approvers and reviewers only, and the README mentions the Netlify Open Source plan without naming an account owner. Because the analytics script is served from redhat.com, access to the data appears to be held by Red Hat staff rather than by the project, and that dependency is not recorded anywhere.
