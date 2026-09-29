# KubeVirt communication methods documented: answers

- Is there a Slack/Discord/Discourse/etc. community and is it prominently linked from your website?

  Yes. KubeVirt uses two channels in the Kubernetes Slack workspace, `#virtualization` for users and `#kubevirt-dev` for contributors. The kubevirt.io home page links to Slack in its footer, and the kubevirt.io Community page has a "Talk to Us!" section that names both channels, links to each, and links to the Kubernetes Slack invitation page so a newcomer can get an account. The kubevirt/community README repeats both channel links.

  In the user guide the link is less prominent. The Welcome page has a "Getting help" section that links to `#virtualization` (as a raw URL rather than a channel name), the GitHub issue tracker, and the mailing list; the Contributing page mentions Slack in passing and points to the Community page. The `#kubevirt-dev` channel is not mentioned in the guide. No other page in the guide links to Slack, and the mkdocs-material header and footer do not carry social or chat icons because `extra.social` and `repo_url` are not configured in `mkdocs.yml`.

- Is there a direct link to your GitHub organization/repository?

  Yes. The kubevirt.io home page and Community page link to the GitHub organization (github.com/kubevirt) and to the main kubevirt/kubevirt repository. The user guide's Welcome page links to the kubevirt/kubevirt issue tracker under "Getting help" and to the API reference under "Developer", and every page has "Edit this page" and "View source" actions that resolve to the kubevirt/user-guide repository. The Contributing page links to the organization, to the user-guide, kubevirt.github.io, community, kubevirt, and containerized-data-importer repositories, and to their issue lists.

  The user guide does not display a repository link in its header, which mkdocs-material provides when `repo_url` is set. A reader must reach the Welcome or Contributing page, or use the edit icon, to find the source repository.

- Are weekly/monthly project meetings documented? Is it clear how someone can join those meetings?

  Yes, in the community repository; only indirectly on the websites. The kubevirt/community repository's `community_meeting.md` documents the weekly community meeting in detail: Zoom meeting ID and join link, time (Wednesdays 16:00 CET/CEST), hosts, the running meeting-notes document, how recordings are produced and posted to the YouTube "Community Meetings" playlist, and that minutes are mailed to kubevirt-dev. The kubevirt.io Community page embeds the KubeVirt community calendar (`kubevirt@cncf.io`) and states that anyone may "join any of our community meetings - no registration required."

  The user guide itself does not mention the community meeting, the calendar, or SIG meetings; its Contributing page links to the Community page and to a New Contributor session recording on YouTube. SIG charters in kubevirt/community (for example `sig-network/charter.md`) do not list meeting times or channels, so SIG meeting cadence is discoverable only through the shared calendar.

- Are mailing lists documented?

  Yes. The kubevirt-dev Google Group is linked from the kubevirt.io home page footer, the Community page, the kubevirt/community README, and the user guide's Welcome page under "Getting help". The community meeting document states that weekly minutes are posted to the list, and the kubevirt/kubevirt pull request template asks authors to consider announcing changes there.

  The list is presented as a bare link with no description of its purpose, expected traffic, or whether it is the right place for user questions versus development discussion. There is no separate user-oriented list, and the guide does not say so. The Contributing page does not mention the mailing list at all.
