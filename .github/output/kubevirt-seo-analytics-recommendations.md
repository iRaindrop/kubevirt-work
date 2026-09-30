# SEO Analytics and Site Search - Recommendations

The following recommendations address the SEO Analytics and Site Search of the KubeVirt user guide.

- Enable analytics on the user guide. Add an `extra.analytics` block to `mkdocs.yml` (Material supports Google Analytics 4 natively, or use a custom `overrides/main.html` partial to load the same Adobe Analytics tag the main site uses) so documentation page views, search terms, and 404 hits are captured.
- Gate analytics to production only. In the main site, wrap the `dpal.js` include in `_includes/head.html` with a check on `jekyll.environment == "production"` and set `JEKYLL_ENV=production` only in the Netlify production context. In the user guide, inject the analytics snippet only when the Netlify `CONTEXT` variable equals `production`, for example by templating it in the `netlify.toml` build command.
- Add an explicit `noindex` for non-production deploys rather than relying on Netlify defaults. Emit `X-Robots-Tag: noindex` from a `_headers` file or a `[context.deploy-preview]` / `[context.branch-deploy]` section in each repository's `netlify.toml`.
- Fix `robots.txt` on kubevirt.io: correct the sitemap URL to `https://kubevirt.io/sitemap.xml` and add a second `Sitemap:` line for `https://kubevirt.io/user-guide/sitemap.xml`.
- Remove the obsolete `sed` line in this repository's `netlify.toml` that rewrites `site_url: https://kubevirt.io/docs`, since `mkdocs.yml` already sets `site_url` to `https://kubevirt.io/user-guide` and the command no longer has any effect.
- Extend the main site's lunr index in `_layouts/search.html` to include `site.pages` in addition to `site.posts` so that non-blog pages are searchable, and add a link from the main site's search page to the user guide search (or vice versa) so users can find documentation from either entry point.
- Document analytics custodianship. Add a short "Site infrastructure" section to the README of each repository (or to the SIG Docs or community repository) that names the owners or aliases responsible for the Adobe Analytics property, the Netlify sites, and Google Search Console, and describes how a maintainer requests access or a 404 report.
- Once analytics are in place, set up a recurring 404 report (for example, a saved report filtered on the not-found page title) and use it to add missing entries to the `redirects` plugin map in `mkdocs.yml`.
