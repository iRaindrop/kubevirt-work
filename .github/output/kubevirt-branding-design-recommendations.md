# Branding and Design - Recommendations

The following recommendations address the branding and design of the KubeVirt user guide.

- Publish a short brand reference, either in the `kubevirt.github.io` repository or in the `community` repository, that lists the canonical logo files (icon and horizontal wordmark), the hex values of the `$kv-color--green-*` scale, and the approved typefaces. Have `docs/stylesheets/extra.css` in the user guide cite that reference in a comment so the two sites stay aligned when the palette changes.
- Align the user guide's brand tokens with the main site's scale. Replace the ad hoc `#0db2b6` primary with a value from the documented scale (for example, `$kv-color--green-300`, `#00aab2`), or add `#0db2b6` to the scale so both properties draw from the same list.
- Add an `extra.social` block and a `copyright` line to `mkdocs.yml` so the Material footer shows the project's GitHub, Slack, and `kubevirt.io` links. This gives readers a visual and navigational link between the guide and the main site at almost no cost.
- Consider using the horizontal `KubeVirt_logo_color.svg` wordmark in the guide's header, or add the wordmark to the main site's header alongside the icon, so both properties present the same logo variant.
- Check the `filter: brightness(80%)` link rule against WCAG AA contrast in both the light and dark schemes. If it fails, replace the filter with explicit `--md-typeset-a-color` values per scheme so the link color is deliberate rather than derived.
- Review the `.md-typeset table:not([class]) { width: max-content; }` rule on a narrow viewport. If wide tables push past the content column, scope the rule to a class applied only to tables that need it, or wrap those tables so they scroll within the column.
- Remove the unused legacy assets `asciibinder-logo-horizontal.png`, `asciibinder_web_logo.svg`, and `book_pages_bg.jpg` from `docs/assets` so the repository contains only current brand assets.
- Remove the unsupported top-level `site_favicon` key from `mkdocs.yml`; MkDocs ignores it and the active favicon is already set under `theme.favicon`.
