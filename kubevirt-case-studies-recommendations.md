# Case Studies - Recommendations

The following recommendations address the case studies of the KubeVirt user guide.

- Link the two existing CNCF case studies (NTT Docomo Business and Swisscom) from `kubevirt.io`, for example in a "Case Studies" block beneath the End Users logo wall on the landing page. This is a quick win: the content already exists and is published by CNCF.
- Extend `adopters.py` and `_data/adopters.yml` to carry the "Use-Case" text from `ADOPTERS.md`, and show it on the website as a tooltip or an expandable card on each logo. This turns the logo wall into a set of short, attributed testimonials at no authoring cost.
- Create a `/adopters/` or `/case-studies/` page on `kubevirt.io` that renders the full adopters table (type, name, since, use case) and links to the CNCF case studies, so evaluators have a single place for adoption evidence. Add it to `_data/site_nav_pages.yml`.
- Invite two or three adopters with strong use-case statements (for example Cloudflare, CoreWeave, or SK Telecom) to expand them into short blog posts or Summit talks, and tag those posts with a `case-study` or `user-story` category so they can be listed together.
- Add a blog category or tag scheme beyond `news` and `uncategorized`, and backfill recent posts, so the blog index can filter by release, feature, community, and user story.
- Set a modest publishing target for the blog, such as one post per KubeVirt minor release plus one community or adopter post per quarter, and track it in the community repository so cadence does not depend on a single author.
- In the user guide, add a short "Community and adoption" block to `docs/index.md` that links to the `kubevirt.io` blog, videos, Summit, adopters or case-studies page, and Slack. Optionally add a top-level "Community" entry to `docs/.nav.yml` that opens the `kubevirt.io/community` page.
- In `docs/contributing.md`, in addition to inviting readers to submit case studies, link to the existing adopters list and case studies so contributors can see the format they are being asked to follow.
