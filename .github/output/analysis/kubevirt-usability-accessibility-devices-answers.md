# KubeVirt usability, accessibility, and devices: answers

- Is the website usable from mobile?

  Yes. The user guide uses mkdocs-material, which is responsive by default, and every page carries a `width=device-width, initial-scale=1` viewport meta tag. On narrow screens the header collapses to a hamburger drawer that contains the section navigation, the page's table of contents, and the search entry point, and the footer offers previous and next page links. A light and dark color scheme toggle is available.

  Two content patterns reduce mobile usability. The site's `extra.css` sets `.md-typeset table:not([class])` to `display: table; width: max-content`, which forces wide tables such as the Arm64 feature-gate and device status pages to their natural width. Whether they remain horizontally scrollable depends on Material's JavaScript table wrapper; this needs verification on a device. Separately, 531 non-table lines in the source exceed 140 characters, most of them single-line commands and YAML in code blocks, which require horizontal scrolling on phones. The 3,000-line Release Notes page is a single document and is slow to load and scroll on mobile.

- Are doc pages readable?

  Yes, in the main. Material's typography, line length, and spacing are used unmodified apart from a slightly larger, teal-colored section label in the sidebar on wide screens and a light border on inline code. Pages use a single `h1` and a sensible heading hierarchy (`h2` through `h5` on Live Migration), admonitions are used for notes and warnings on newer pages, and footnotes and permalinks are enabled.

  Readability varies with page age. Older pages such as Installation, Lifecycle, and Disks and Volumes present commands as indented blocks with `$` prompts and mix command and output in one block, which is harder to scan than the fenced, language-tagged blocks on newer pages. The Architecture page conveys its central "stack" diagram as ASCII art in a preformatted block, and several long pages (Live Migration at 500 lines, Disks and Volumes at over 1,300 lines, Interfaces and Networks at about 700 lines) have no in-page summary or grouping beyond the table of contents.

- Are all / most website features accessible from mobile -- such as the top-nav, site search and in-page table of contents?

  Yes. Material moves the top-level tabs into the drawer on mobile, the search icon opens a full-screen search overlay, and the in-page table of contents appears inside the drawer under the current page. The Welcome, Architecture, Quickstarts, Release Notes, and Contributing pages hide the navigation sidebar via front matter (`hide: navigation`), so on those pages the drawer shows only the table of contents; the section list on the Welcome page is prose rather than links, so a mobile reader must open the drawer to move into a section.

- Are color contrasts significant enough for color-impaired readers?

  Mostly, with one clear failure. The site overrides Material's teal palette with a custom primary color, `#0db2b6`. White text on that color, which is how the header bar, tabs, and site title render, has a contrast ratio of about 2.6:1, below the WCAG AA minimum of 4.5:1 for normal text and 3:1 for large text. Body links use the primary color darkened to 80 percent brightness (about `#0a8e92`), giving roughly 3.96:1 on white, which passes for large text but not for normal body text. The sidebar section labels (`#00797f`, 5.2:1) and the accent color (`#006166`, 7.2:1) pass.

  The site does not rely on color alone. Active tabs are underlined as well as colored, links are distinguished by color and hover underline, and admonitions carry icons and titles in addition to colored borders. The dark scheme uses the same primary color, so the header contrast issue persists in dark mode while link contrast improves slightly (about 4.06:1 on the slate background).

- Are most website features usable using a keyboard only?

  Yes. Material provides a "Skip to content" link as the first focusable element, the search field is reachable by Tab and by the `/` or `s` shortcut, search results are navigable with arrow keys, and the navigation drawer, table of contents, tabs, color toggle, and previous and next links are standard focusable controls. The rendered page contains 47 `aria-label` attributes on controls. The site adds no custom JavaScript that would trap or hide focus. Code blocks have no copy button, so there is nothing to reach; enabling one would add a keyboard-accessible control.

- Does text-to-speech offer listeners a good experience?

  Partially. Pages declare `lang="en"`, use real headings for structure, and label controls with ARIA attributes, so a screen reader can announce structure and navigate by heading. The two images on the Windows Virtio Drivers page have descriptive alt text ("Choose driver", "Install driver", and so on).

  Content patterns work against listeners. The Architecture page's ASCII stack diagram will be read as a stream of plus signs, pipes, and tildes with no textual equivalent. Indented code blocks with `$` prompts are announced as "dollar" before each command. Long YAML manifests and `kubectl` output tables are read line by line with no summary of what they show. The logo image's alt text is "logo" rather than "KubeVirt". Wide status tables (for example the Arm64 feature-gate table with a status column per gate) are readable but tedious without a caption or summary row.
