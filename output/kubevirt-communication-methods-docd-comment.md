# KubeVirt communication methods documented: comment

KubeVirt's communication channels are well established and thoroughly documented at the community level. Two Slack channels, a Google Group, a GitHub organization, a public community calendar, a weekly Zoom meeting with recorded sessions on YouTube, and posted minutes are all in place, and the kubevirt/community repository describes the meeting mechanics in more detail than most CNCF projects. The kubevirt.io Community page gathers the channels, the calendar, and the Slack invitation link on one page, and the home page footer repeats the primary links.

The gap is in how the user guide surfaces these channels. A user who hits a problem while following a page has no path to help except to return to the Welcome page, where "Getting help" offers three bare URLs with no guidance on which channel suits which question. The guide does not mention the `#kubevirt-dev` channel, the community meeting, the calendar, or that meeting minutes are mailed to kubevirt-dev, and the mkdocs-material header and footer carry no repository or social icons because `repo_url` and `extra.social` are not set. Meeting details live only in the community repository; the websites present a calendar embed and a one-line invitation without stating the day, time, or how to join. SIG charters do not record meeting cadence, so SIG-level participation depends on scanning the shared calendar.

Strengths:

- Two purpose-specific Slack channels, a mailing list, a public calendar, and a weekly recorded meeting are all active and linked from kubevirt.io.
- `community_meeting.md` documents Zoom details, time, hosts, notes, recordings, and minutes distribution in depth.
- The Community page links the Kubernetes Slack invitation page so newcomers can get an account.
- Every user guide page has edit and view-source actions pointing at the repository.
- The Contributing page links every relevant repository and issue list.

Weaknesses:

- The user guide's only help section is on the Welcome page and consists of bare URLs without guidance on which channel to use.
- No repository, Slack, or mailing list icons in the guide's header or footer.
- The community meeting, calendar, and `#kubevirt-dev` channel are not mentioned in the user guide.
- Meeting day, time, and join instructions appear only in the community repository, not on kubevirt.io.
- SIG charters do not list meeting times or channels.

Rating: 4 - Meets or exceeds standards
