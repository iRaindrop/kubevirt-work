# Maintenance Planning - Answers

- Is the website tooling well supported by the community (i.e., Hugo with the Docsy theme) or commonly used by CNCF projects?

  Yes. The user guide is built with MkDocs and the Material for MkDocs theme, plus the `mkdocs-awesome-nav` and `mkdocs-redirects` plugins. All four are actively maintained, widely used open-source projects, and MkDocs Material in particular is common among CNCF and Kubernetes-ecosystem projects. The main website (kubevirt.io) is a Jekyll site with a hand-built Bootstrap 4 layout and a dozen Jekyll plugins; Jekyll is mature and well supported but is less common among CNCF projects than Hugo or Docusaurus, and the custom theme means design changes fall entirely on the project. The two sites use different static-site generators, so maintainers need to know both toolchains.

- Is there active cultivating website maintainers from within the community?

  Only informally. Both repositories have `OWNERS` files with active reviewer and approver lists, and the main website's `OWNERS` file records emeritus approvers with dates, which shows the roster is periodically pruned. The website README explicitly invites UI/UX developers to pick up `kind/website` issues, and the user guide README says contributions are welcome. However, there is no documented path from contributor to website maintainer, and the community `sig-list.md` shows a `sig/documentation` label with no chairs or members. Commit history over the past year shows one person (`aburdenthehand`) as the top human committer in both repositories, with most other contributions coming from feature authors documenting their own work or from Dependabot.

- Are site build times reasonable?

  Yes. Both sites are built by a Prow postsubmit job that runs `make build` and pushes the output to a `gh-pages` branch served by GitHub Pages. Comparing commit timestamps on `main` with the corresponding "Postsubmit site update" commits on `gh-pages` shows the user guide is republished within about 40 seconds of a merge and the main website within about 90 seconds. Pull-request previews for the user guide build on Netlify from a pinned `netlify.toml` command that installs MkDocs with `pip` on every build. The `netlify.toml` still contains a `sed` step that targets an obsolete `site_url` value and does nothing, which is harmless but suggests the file has not been reviewed recently.

- Do site maintainers have adequate permissions?

  Partly documented. Merging is governed by Prow and the `OWNERS` files, so approvers can land content changes without additional access. Deployment is fully automated through the `kubevirt-bot` account, which pushes to `gh-pages`, so no maintainer needs push rights to the published branch. Access to the supporting services is not documented: nothing in either repository states who can administer the Netlify site (`kubevirt-user-guide`), the GitHub Pages and custom-domain settings, DNS for kubevirt.io, or the Prow job definitions in `kubevirt/project-infra`. Whether current approvers hold those permissions cannot be determined from the repositories.

- Is the website accessible via HTTPS?

  Yes. Both `https://kubevirt.io/` and `https://kubevirt.io/user-guide/` are served over HTTPS by GitHub Pages with a valid certificate for the custom domain. The Netlify preview alias `https://kubevirt-user-guide.netlify.app/` is also served over HTTPS.

- Does HTTP access, if any, redirect to HTTPS?

  Yes. Requests to `http://kubevirt.io/`, `http://www.kubevirt.io/`, and `http://kubevirt.io/user-guide/` all return `301 Moved Permanently` to the HTTPS equivalent (with `www` also collapsing to the bare domain), and the Netlify alias redirects HTTP to HTTPS as well. The production responses do not include a `Strict-Transport-Security` header, so browsers rely on the redirect rather than HSTS to enforce HTTPS on repeat visits.
