# Branding and Design - Comment

The KubeVirt user guide has a clear, recognizable identity. The teal heptagon mark, the teal Material palette pinned to the project's own hex values, and the coordinated sidebar label color together make every page unmistakably KubeVirt. Because the branding is configured once in `mkdocs.yml` and `docs/stylesheets/extra.css` rather than in individual pages, it stays consistent across the roughly one hundred pages of the guide and across the light and dark schemes without any effort from content authors. This is the right model for a documentation site and is worth pointing to as an example.

The main gap is that KubeVirt's brand is expressed in two different ways on its two web properties. The main `kubevirt.io` site carries a documented SCSS color scale, the horizontal wordmark, and Open Sans; the user guide carries three copied hex values, the square icon, and Roboto. The colors are from the same family, so nothing looks wrong, but there is no single source of truth for the brand, and the guide's header and footer give the reader no visual or navigational cue that it belongs to the larger site. Unused assets from a previous site generator also remain in the repository.

Typography is clean and well-suited to reading long technical pages, with a sensible pairing of proportional and monospaced faces and good default spacing. The only design choices worth a second look are the small custom CSS rules that darken all links and let tables grow to their natural width, since both trade a little readability for a stylistic or layout effect.

Strengths:

- Distinctive logo mark and brand colors applied at the theme level, so branding is uniform on every page.
- Light and dark schemes share the same brand palette.
- Default Material typography (Roboto and Roboto Mono) is legible and consistently applied to prose, tables, and code.
- Brand colors match the color family the main website defines, so the two properties feel related.

Weaknesses:

- The user guide and `kubevirt.io` use different logo variants, typefaces, and header and footer treatments, with no shared brand definition to keep them aligned.
- The guide's header and footer contain no link back to `kubevirt.io` or to the project's community channels.
- The `filter: brightness(80%)` link rule and the `max-content` table rule have not been checked for contrast and small-viewport behavior.
- Legacy AsciiBinder logos and a background image remain in `docs/assets` without being used.

Rating: 4 - Meets or exceeds standards
