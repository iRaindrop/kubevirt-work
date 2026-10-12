# Website Requirements - Comment

The main KubeVirt website satisfies the CNCF Website Guidelines almost completely. It lives in the project's GitHub organization with DCO enforced, avoids origin-company references and lead capture, alphabetizes its vendor list, and carries a footer with the correct incubating-project statement, the Series LLC copyright wording, the CNCF logo, and a link to the LF Projects policies page that covers trademarks. The footer alone is a good model for other incubating projects to copy.

The user guide, which is where most documentation traffic lands, inherits none of this. Its footer contains no copyright notice, no CNCF affiliation statement or logo, and no trademark or policy link, because the MkDocs configuration never sets a `copyright` value or overrides the footer partial. Since the guide is served on the same `kubevirt.io` domain, a visitor reading documentation sees a site with no visible connection to CNCF or the Linux Foundation. This is the single largest gap against the checklist and is a small configuration change.

Smaller items round out the picture: about a third of the vendor logos link to generic corporate homepages that do not mention KubeVirt, neither repository has a root `CODE_OF_CONDUCT.md` (both rely on the organization default), and the website repository has no `CONTRIBUTING.md` of its own.

Strengths:

- Both sites hosted in the `kubevirt` organization with DCO enforced on every pull request.
- Main website footer includes the correct maturity statement, Series LLC copyright, CNCF logo, and LF Projects policies link.
- No origin-company references or enterprise lead capture; vendor list is alphabetized and sourced from `ADOPTERS.md`.
- `LICENSE` present in both repositories and `CONTRIBUTING.md` in the user guide.

Weaknesses:

- User guide footer has no copyright, CNCF branding, or trademark link.
- Several vendor logos link to corporate homepages rather than KubeVirt support pages.
- No root `CODE_OF_CONDUCT.md` in either repository; no `CONTRIBUTING.md` in the website repository.
- Main website copyright line omits the © symbol.

Rating: 3 - Meets standards
