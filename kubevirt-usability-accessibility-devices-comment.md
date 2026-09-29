# KubeVirt usability, accessibility, and devices: comment

The KubeVirt user guide inherits a solid usability and accessibility baseline from mkdocs-material. The site is responsive, the navigation, search, and table of contents all work from a mobile drawer, keyboard users get a skip link, search shortcuts, and standard focusable controls, and pages declare a language and use a proper heading hierarchy. The project has customized the theme lightly and, apart from color, has not undermined these defaults. Dark mode is available and previous and next links help linear reading.

The one clear defect is color contrast. The custom teal primary color produces white-on-teal header and tab text at roughly 2.6:1 and body links at roughly 4:1, both below WCAG AA for normal text. This affects every page and is a one-line CSS change to fix. The remaining issues are in content rather than the platform: the Architecture page's central diagram is ASCII art with no textual equivalent, older pages use `$`-prefixed indented code blocks that read poorly on screen readers and scroll horizontally on phones, several pages exceed 500 lines without internal grouping, and wide status tables and long command lines depend on horizontal scrolling on small screens. The `width: max-content` table override in `extra.css` should be verified on a real device to confirm tables still scroll rather than overflow the viewport.

Strengths:

- Responsive mkdocs-material theme with viewport meta, mobile drawer navigation, full-screen search, and in-drawer table of contents.
- Skip-to-content link, search keyboard shortcuts, and ARIA-labeled controls out of the box.
- `lang="en"`, single `h1`, and consistent heading hierarchy on pages.
- Light and dark schemes with a toggle; active tabs underlined as well as colored.
- Descriptive alt text on the Windows driver screenshots.

Weaknesses:

- Header and tab text on the custom teal primary color fails WCAG AA (about 2.6:1); body links are borderline (about 4:1).
- The Architecture stack diagram is ASCII art with no text alternative.
- Older pages use `$`-prefixed indented code blocks mixed with output.
- Very long pages (Disks and Volumes, Interfaces and Networks, Live Migration, Release Notes) with no internal grouping.
- Wide tables and 500-plus long code lines require horizontal scrolling on mobile; the `max-content` table override needs device verification.
- Logo alt text is "logo" rather than the project name; no code copy button.

Rating: 3 - Meets standards
