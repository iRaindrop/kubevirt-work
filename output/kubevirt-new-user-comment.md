# New User Content - Comment

The KubeVirt user guide has the ingredients of good new-user content but does not assemble them into a path. Installation is accurate, the four-command operator install works on x86_64 and Arm64, and the Welcome page points to live Killercoda scenarios, minikube and kind quickstarts, and four hands-on labs. Where pages have been recently revised, such as Creating VirtualMachines by using virtctl and Accessing Virtual Machines, the examples are clean fenced blocks a reader can paste. Compared with the Falco getting-started documentation that the CNCF criteria cite as a good example, KubeVirt has equivalent installation depth but lacks Falco's single labeled entry point, per-platform install tabs, and explicit "next steps" hand-off.

The central weakness is that the guide outsources the first-run experience. Quickstarts is a bare link list, Installation is a cluster administrator's reference that buries the core procedure under compatibility notes and legacy distributions and ends without a next step, and the pages a new user needs afterward (`virtctl`, create, access) sit in a different section with no cross-links from Installation or Basic Use. The oldest pages in that chain, Basic Use and Lifecycle, reference a `vmi.yaml` that is never shown, so the first commands a reader encounters cannot be run. Client platform coverage for `virtctl` stops at Linux amd64.

Copy-paste quality is uneven and tracks page age: newer pages use fenced blocks, older ones use `$`-prefixed indented blocks mixed with output, and the theme's copy button is not enabled. These are low-effort fixes with a high payoff for new users.

Strengths:

- Installation gives a correct, short operator-based procedure with expected output and a software-emulation fallback.
- The Welcome page links to live Killercoda scenarios, quickstarts for minikube, kind, and cloud providers, and four hands-on labs.
- Arm64 platform status is documented in a dedicated sub-section.
- Recently revised pages provide clean, pasteable manifests and `virtctl` pipelines.
- Requirements are stated up front, including `--allow-privileged=true` and hardware virtualization validation.

Weaknesses:

- No page labeled "Getting started" and no single in-guide path from install to first running VM.
- Installation mixes the core procedure with AppArmor, kernel compatibility, OKD, k3OS, developer builds, and node placement, and ends without a next step.
- `virtctl` install covers only Linux amd64 via `wget`; macOS, Windows, and arm64 binaries and `PATH` setup are not mentioned.
- Basic Use and Lifecycle reference `vmi.yaml` without providing it and do not link onward.
- Older pages use `$`-prefixed indented code blocks interleaved with output, and the copy button is not enabled.
- The Quickstarts page has no introduction, prerequisites, or outcome statement.

Rating: 3 - Meets standards
