# Website Requirements - Recommendations

The following recommendations address the website requirements of the KubeVirt user guide.

- Bring the user guide footer into compliance. Set `copyright: "Copyright © KubeVirt a Series of LF Projects, LLC"` in `mkdocs.yml`, and add an `overrides/partials/copyright.html` (or a `footer.html` override) that appends "We are a Cloud Native Computing Foundation incubating project", the CNCF logo linked to `cncf.io`, and a link to `https://lfprojects.org/policies/` for trademark and terms. Match the wording and links used in the main website footer so the two properties read as one.
- Add the © symbol to the main website copyright line in `_includes/footer.html` so it reads "Copyright © KubeVirt a Series of LF Projects, LLC".
- Point vendor logos at KubeVirt-specific pages. For each entry in `ADOPTERS.md` whose link is a corporate homepage (Microsoft, Oracle, SUSE, Red Hat, NCR Voyix, TrueFullstaq), ask the vendor for a URL that mentions KubeVirt support or their KubeVirt-based product, and update the link; drop the logo from the Vendors section if none exists.
- Add a root `CODE_OF_CONDUCT.md` to both `kubevirt/user-guide` and `kubevirt/kubevirt.github.io` that links to the `kubevirt/community` code of conduct, so the file is present where the checklist expects it rather than only inherited from the organization default.
- Add a `CONTRIBUTING.md` to `kubevirt/kubevirt.github.io` that points to the existing contributing content in its README and to the user guide's contributing page.
- Update the maturity statement in both footers when the project's CNCF status changes, and add a note in each repository's README naming the file to edit so the statement does not go stale.
