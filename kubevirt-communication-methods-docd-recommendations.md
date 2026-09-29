# KubeVirt communication methods documented: recommendations

The following recommendations address the communication methods documented of the KubeVirt user guide.

- Configure `repo_url: https://github.com/kubevirt/user-guide` and `repo_name` in `mkdocs.yml` so the repository link appears in the site header, and add `extra.social` entries for GitHub, Slack, the kubevirt-dev Google Group, YouTube, and Bluesky so the icons appear in the footer of every page.
- Expand the Welcome page's "Getting help" section into a short guide to channels: use `#virtualization` on Kubernetes Slack for usage questions, `#kubevirt-dev` and the kubevirt-dev mailing list for development discussion and design proposals, GitHub issues for bugs and feature requests, and the weekly community meeting for live discussion. Link the Kubernetes Slack invitation page next to the channel names.
- Add a "Community and meetings" subsection to the Contributing page that states the community meeting day and time, links the Zoom join link, the community calendar, the meeting notes document, and the YouTube Community Meetings playlist, and explains that minutes are posted to kubevirt-dev.
- Add a "Need help?" admonition or footer snippet to the Installation, Accessing Virtual Machines, and Debug pages, and to any future Troubleshooting page, that links to the Getting help section so users can reach a channel from where problems occur.
- On the kubevirt.io Community page, add the community meeting day, time, and Zoom link next to the calendar embed, and a one-line description under each channel stating what it is for.
- Ask the SIG leads to add a "Meetings and communication" section to each SIG charter in kubevirt/community listing the SIG's meeting cadence, calendar entry, and Slack channel, and link the SIG list from the user guide's Contributing page.
- Describe the kubevirt-dev mailing list's purpose wherever it is linked, and state explicitly that there is no separate user list so that users know to use Slack or the same list for questions.
