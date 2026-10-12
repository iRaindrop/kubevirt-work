# Website Requirements - Answers

- Are most of the applicable CNCF Website Guidelines satisfied? See https://github.com/cncf/techdocs/blob/main/docs/website-guidelines-checklist.md

  Yes for the main website, and only partly for the user guide. KubeVirt is a CNCF incubating project, so the "developing" standard applies. Taking the checklist items in order:

  1. Open source repository. Both sites are hosted in the `kubevirt` GitHub organization alongside the main project: the website in `kubevirt/kubevirt.github.io` and the user guide in `kubevirt/user-guide`. Both repositories run the DCO check on every pull request (it appears as a required `dco` status alongside `tide` and the Netlify preview), and the user guide README explains how to sign commits.

  2. Origin company. The homepage does not refer to Red Hat as the originator; Red Hat appears only as one logo among the alphabetized End Users and Vendors lists.

  3. Enterprise support leads. There are no lead-capture links or forms on either site; the only forms are the search boxes and the user guide's color-scheme toggle. The homepage has a Vendors section of eighteen logos, sorted alphabetically, populated from `ADOPTERS.md` through a documented process, which serves as the vetting step.

  4. Vendor links. Several vendor logos link to pages that describe the vendor's KubeVirt offering (Kubermatic, Platform9, Spectro Cloud, KubeSphere), but others link to the vendor's generic corporate homepage (Microsoft, Oracle, SUSE, Red Hat, NCR Voyix, TrueFullstaq), which does not mention KubeVirt support.

  5. Copyright notice. The main website footer reads "Copyright KubeVirt a Series of LF Projects, LLC", which is the wording the checklist specifies for projects converted to the Series LLC model, though it omits the © symbol. The user guide footer contains only "Made with Material for MkDocs" and no copyright notice; `mkdocs.yml` sets no `copyright` value.

  6. CNCF branding. The main website footer states "We are a Cloud Native Computing Foundation incubating project", which matches the project's current maturity level, and displays the CNCF color logo linked to `cncf.io`. The user guide has no CNCF statement or logo anywhere on the page.

  7. Footer trademark and policy links. The main website footer links to `https://lfprojects.org/policies/` "for website terms of use, trademark policy and other project policies", which satisfies the trademark-guidelines requirement through a terms page. The user guide footer has no trademark or policy link.

  Community and license files. Both repositories have a `LICENSE` file. The user guide has a `CONTRIBUTING.md`; the website repository has none, though its README covers contributing in detail. Neither repository has a `CODE_OF_CONDUCT.md` in its root; GitHub applies the organization-wide default from the `kubevirt/.github` repository, so the code of conduct is visible on the repository page but is not a file in the repository as the checklist asks.
