# Branding and Design - Answers

- Is there an easily recognizable brand for the project (logo + color scheme) clearly identifiable?

  Yes. The KubeVirt user guide displays the project's teal heptagon logo (`docs/assets/KubeVirt_icon.png`) in the site header and uses it for the favicon (`favicon32x32.png`). The `mkdocs.yml` theme configuration selects the Material `teal` palette for both the light and dark color schemes, and `docs/stylesheets/extra.css` pins the primary color to `#0db2b6` and the accent color to `#006166`. Navigation section labels in the sidebar use a third brand tone, `#00797f`.

  The colors come from the same family the main `kubevirt.io` website defines in `_sass/_colors.scss` as `$kv-color--green-300` through `$kv-color--green-700` (for example, `#00797f` and `#006166`). The logo mark itself is distinctive and is the only mark used in the guide's chrome, so a reader landing on any page can identify the site as KubeVirt immediately.

- Is the brand used across the website consistently?

  Yes, within the user guide. Logo, favicon, and palette are set once at the theme level, so every page renders the same header, colors, and active-tab underline without any per-page effort from authors. The dark scheme reuses the same teal primary and accent values, so switching modes keeps the brand intact.

  Consistency across the project's two web properties is partial. The main `kubevirt.io` site is a Jekyll and Bootstrap site that uses the horizontal wordmark `KubeVirt_logo_color.svg`, the Open Sans typeface, and a fully documented SCSS color scale, while the user guide uses the square icon-only mark, Roboto, and three hand-copied hex values. The two sites share the color family and logo mark but differ in logo variant, typography, header layout, and footer, so the transition between them is noticeable. The user guide's `mkdocs.yml` defines no `extra.social` links or `copyright` footer, and the `docs/assets` directory still contains legacy assets from a previous site generator (`asciibinder-logo-horizontal.png`, `asciibinder_web_logo.svg`, `book_pages_bg.jpg`) that are not referenced by any page.

- Is the website's typography clean and well-suited for reading?

  Yes. The guide does not override the Material theme fonts, so it inherits Roboto for body text and Roboto Mono for code, loaded from Google Fonts. Headings, body copy, admonitions, tables, and syntax-highlighted code blocks all use these two faces at Material's default sizes and line heights, which are tuned for long-form technical reading. Inline code receives a light `1px` border from `extra.css`, which helps distinguish identifiers from prose.

  Two custom rules affect readability. `.md-nav a, .md-typeset a { filter: brightness(80%); }` darkens all link text, including links inside the dark scheme, and its effect on contrast has not been verified. `.md-typeset table:not([class]) { width: max-content; }` lets wide tables extend past the content column and rely on horizontal scrolling, which is useful for the many API-field tables but can crowd narrow viewports. Typography differs from the main site, which uses Open Sans at a 16px base.
