# KubeVirt information architecture: answers

- Is there high level conceptual content?

    Yes. The Architecture page gives a conceptual overview of the KubeVirt stack, explains how CRDs, controllers, and node daemons extend Kubernetes, and describes each component (`virt-api`, `virt-controller`, `virt-handler`, `virt-launcher`). Several feature pages open with a short overview before the procedure, for example Live Migration, Run Strategies, and VirtualMachine Templates.

    Conceptual content is thin at the section level. The Welcome page describes each top-level section in one line, but the Compute, Network, and Storage sections have no landing or overview page that explains how their pages relate or which one a reader needs first. The User Workloads section relies on the two-paragraph Basic Use page and the Lifecycle page for its conceptual framing.

- Is the documentation feature complete?

    Mostly. The guide covers the core VirtualMachine and VirtualMachineInstance lifecycle, instance types and preferences, pools, replica sets, templates, live migration, hotplug of CPU, memory, volumes, and interfaces, snapshots and restore, clone, export, network binding plugins, feature gates, node maintenance, confidential computing, and debugging. The Arm64 pages document per-architecture device and feature-gate status.

    Some recently released features have no page. The v1.9.0 release notes describe the `VirtualMachineBackup` API, the `CrossArchitectureVirtualization` feature gate, masquerade `PortRanges`, and MigrationPolicy compression, but none of these terms appears outside the release notes. The new Plugins page exists in `cluster_admin/` but is absent from the section `.nav.yml`, so it is reachable only from a link on the deprecated Hook Sidecar page.

- Are there step-by-step instructions documented for features in tasks and tutorials?

    Yes, for most features. Pages such as Accessing Virtual Machines, Creating VirtualMachines by using virtctl, Live Migration, Hotplug Volumes, and Snapshot and Restore API pair a short explanation with manifests and commands the reader can run. The Debug page and the Virtualization Debugging section walk through log verbosity, privileged node debugging, and launching QEMU under `strace` and `gdb`.

    The guide does not contain a tutorial of its own. The Quickstarts page and Welcome page link out to Killercoda scenarios, kubevirt.io quickstarts, and kubevirt.io labs for the guided "install, create a VM, connect to it" experience.

- Are there any key features that are documented but missing task documentation?

    Yes. Basic Use lists four `kubectl` commands and states that the following pages describe how to use the API, but it does not include a sample `vmi.yaml` or link to a page that does. Lifecycle shows `kubectl create -f vmi.yaml` without a manifest. The Architecture page describes components without linking to the operational pages that configure them. The Plugins page describes domain hooks and node hooks at Alpha but is not integrated into the navigation.

- Is the "happy path" (most common use case) documented?

    Partially. Installation, `virtctl` installation, creating a VirtualMachine with `virtctl create vm`, starting and stopping it, and connecting over console, VNC, or SSH are all documented. However, these steps sit on five different pages across two sections, and no single page strings them together for a first-time reader. The Welcome page delegates that path to external labs.

- Are tasks clearly named according to user goals?

    Mixed. User Workloads pages use goal-oriented names such as "Creating VirtualMachines by using virtctl", "Accessing Virtual Machines", and "Boot from external source". Many Compute, Network, and Storage pages are named for the feature or API rather than the task, for example "Clone API", "Export API", "Snapshot Restore API", "Migration Controller", "CSI Overlay", and "Virtual Hardware". Cluster Administration mixes both styles ("Activating and deactivating feature gates" next to "KSM" and "Scheduler").

- If the documentation doesn't suffice, is there a clear escalation path for users needing more help? (FAQ, Troubleshooting)

    Partially. The Welcome page has a Getting Help section that links to the GitHub issue tracker, the kubevirt-dev mailing list, and the Kubernetes Slack channel. The Virtualization Debugging section is the closest thing to troubleshooting content and is aimed at developers and advanced users.

    There is no FAQ and no user-facing troubleshooting page that lists common symptoms (VMI stuck in `Scheduling`, migration failures, console access errors) with causes and fixes. Troubleshooting notes exist but are scattered inside individual feature pages such as Accessing Virtual Machines ("Debugging console access") and Memory Dump.

- If the product exposes an API, is there a complete reference that includes documented CLIs as applicable?

    Partially. The Welcome page links to the generated API reference at kubevirt.io/api-reference, and individual pages deep-link into it where relevant. There is no `virtctl` command reference in the guide. The `virtctl` page covers only download and installation, and command usage is distributed across feature pages (`create vm`, `start`, `stop`, `pause`, `migrate`, `addvolume`, `vnc`, `ssh`, `port-forward`). Feature gates are documented by procedure but the guide does not maintain a list of gates and their stages; the release notes are the only place that records graduations.

- Is content up to date and accurate?

    Largely, with visible legacy pockets. Recently updated pages carry version-stamped feature-state banners (VirtualMachine Templates, Hook Sidecar, Hotplug Volumes), and deprecated mechanisms such as presets, the OpenShift-based Templates page, and the Hook Sidecar are labeled and point to replacements. Release notes extend to v1.9.0.

    Older content shows its age. Installation still documents installing from the OKD Service Catalog as an Ansible Playbook Bundle and installing on k3OS, and links to OpenShift 4.10 documentation. Basic Use and Lifecycle were last touched in May 2024 and still frame VirtualMachineInstance as the primary object, while the rest of the guide and `virtctl create vm` center on VirtualMachine. `compute/windows_virtio_drivers.md` is a byte-identical, unlisted duplicate of `user_workloads/windows_virtio_drivers.md`.

- Does the documentation need restructuring?

    Not a full restructure. The 2024 move from a flat `operations/` and `virtual_machines/` layout into audience- and layer-based sections (Cluster Administration, User Workloads, Compute, Network, Storage) with explicit `.nav.yml` ordering and redirects is sound. The remaining problems are within sections rather than between them: the User Workloads section mixes lifecycle basics, Windows guidance, monitoring, and a "Workloads" sub-group of nine pages that includes deprecated presets and both template mechanisms; long Compute and Storage lists have no internal grouping or landing page; and five pages exist outside the navigation. Release Notes, a 3,000-line page, sits in the main navigation between Storage and Contributing.
