# KubeVirt new user content: answers

- Is "Getting started" clearly labeled? (e.g "Getting started", "Installation", "First steps", etc.)

    Partially. The main navigation has a "Quickstarts" tab and the Cluster Administration section opens with "Installation", so both labels a new user would scan for are present. There is no page titled "Getting started" or "First steps", and the Welcome page describes Quickstarts as "a list of resources to help you learn KubeVirt basics" rather than as the place to begin.

    The Quickstarts page itself is a list of four external links (Killercoda, minikube, kind, cloud providers) with no introduction, prerequisites, or statement of what a reader will have accomplished at the end. The `virtctl` page, which a new user needs immediately after installation, is titled "Download and Install the virtctl Command Line Interface" and sits sixth in the User Workloads section rather than next to Installation.

- Is installation documented step-by-step?

    Yes. The Installation page lists requirements (a supported Kubernetes version, `--allow-privileged=true`, `kubectl`), explains how to validate hardware virtualization with `virt-host-validate`, and gives a four-command sequence that fetches the latest release tag, applies the operator manifest, applies the KubeVirt custom resource, and waits for the `Available` condition. It then shows the expected `kubectl get pods -n kubevirt` output and explains how to enable software emulation when KVM is unavailable.

    The page is long and mixes the core procedure with content a first-time user does not need: AppArmor integration, host kernel and userland compatibility, SELinux, OKD Service Catalog, k3OS, daily developer builds, deploying from source, network plugin installation, and node placement. The core install commands appear roughly 130 lines into the page. Notes about behavior "prior to release v0.20.0" and "prior to KubeVirt 0.34.2" remain in the main flow. The page ends with node-placement patches and does not tell the reader what to do next.

- If needed, is guidance provided for multiple operating systems and platforms?

    Partially. Installation states that the operator supports x86_64 and Arm64, and a dedicated "ARM cluster" sub-section documents Arm64 feature-gate status, device status, unsupported operations, and VM specifics. Container runtime, AppArmor, and SELinux considerations are covered for Linux hosts. Kubernetes distribution coverage includes generic Kubernetes, OKD, and k3OS, with minikube, kind, and cloud providers delegated to external quickstarts.

    Client-side platform guidance is missing. The `virtctl` page shows only a `wget` for `virtctl-${VERSION}-linux-amd64` and does not mention the macOS, Windows, or arm64 binaries that the release page publishes, nor how to make the binary executable and place it on the `PATH`. Guest operating systems are covered for Windows (virtio drivers, legacy Windows) but there is no equivalent "your first Linux guest" page; Linux examples rely on containerDisk images referenced in scattered manifests.

- Do users know where to go after reading the getting started guide?

    No. Installation ends without a next-step link. The Quickstarts page has no "what next" section. Basic Use tells the reader that "the following pages describe how to use and discover the API, manage, and access virtual machines" but does not link to any of them. The Welcome page lists the sections but does not suggest a reading order. A new user who finishes installing has to infer that User Workloads is the next section and that Creating VirtualMachines by using virtctl and Accessing Virtual Machines are the relevant pages.

- Is your new user content clearly discoverable, such as on the documentation home page?

    Yes, with caveats. The Welcome page has a "Try it out" section linking to Killercoda and the quickstarts and a "KubeVirt Labs" section linking to four hands-on labs on kubevirt.io. Quickstarts is the third item in the top navigation. Both the quickstarts and the labs resolve and are current.

    The discoverable new-user content is almost entirely external to the user guide. Within the guide, the reader must open Cluster Administration to find Installation and User Workloads to find `virtctl`, creation, and access. The Welcome page hides its own navigation sidebar, so the section descriptions and the "Try it out" links are the only cues.

- Is there sample code or content that can easily be copy-pasted?

    Yes, with friction. Nearly every page includes manifests and commands. Recently written pages such as Creating VirtualMachines by using virtctl, Accessing Virtual Machines, and VirtualMachine Templates use fenced `shell` or `yaml` blocks without prompt characters. Instance type and preference examples and the `virtctl create vm` pipelines can be pasted directly.

    Older pages, including Installation, Lifecycle, `virtctl`, Disks and Volumes, and Export API, use indented code blocks prefixed with `$ `, which paste as invalid commands and are interleaved with example output. The mkdocs-material `content.code.copy` feature is not enabled in `mkdocs.yml`, so there is no copy button on code blocks. Basic Use and Lifecycle reference `vmi.yaml` without supplying the manifest, so the first commands a new user meets cannot be run as written.
