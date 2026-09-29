# KubeVirt information architecture: comment

The KubeVirt user guide has a sound top-level information architecture. Content is grouped by audience and layer (Cluster Administration, User Workloads, Compute, Network, Storage, Virtualization Debugging), ordering is controlled deliberately through `.nav.yml` files, and the redirects map shows the project maintained old URLs when it reorganized. Most feature pages follow a consistent pattern of a short concept, a feature-state banner where relevant, and runnable manifests or `virtctl` commands. Deprecated mechanisms are labeled and point to their replacements. Compared with the Prometheus documentation, which the CNCF criteria cite as a good example, the KubeVirt guide has comparable feature coverage but lacks Prometheus's clear "Getting started" spine and its consolidated reference material.

The main weakness is that the guide is a well-organized encyclopedia rather than a guided path. A new user must assemble the happy path from Installation, the `virtctl` install page, Creating VirtualMachines, Lifecycle, and Accessing Virtual Machines, and the guide points to external Killercoda and kubevirt.io labs to fill that gap. The oldest foundational pages (Basic Use, Lifecycle) still present VirtualMachineInstance as the primary object, which is out of step with the VirtualMachine-centric approach used everywhere else. Reference material for `virtctl` and for feature gates is not consolidated, and there is no user-facing troubleshooting or FAQ page, so the escalation path jumps straight from feature pages to Slack and GitHub issues.

Currency is uneven. New v1.9 features are documented where a page exists (VirtualMachine Templates, Plugins), but the Plugins page is not in the navigation, several v1.9 APIs and feature gates appear only in release notes, and Installation still carries legacy OKD Service Catalog and k3OS content. Section-internal organization is the other systemic issue: Compute and Storage are long flat lists named after APIs rather than user goals, and the User Workloads "Workloads" sub-group mixes current, legacy, and deprecated mechanisms without signaling which one a reader wants.

Strengths:

- Audience- and layer-based top-level sections with explicit, intentional page ordering.
- Redirects preserve old `operations/` and `virtual_machines/` URLs after the reorganization.
- Consistent feature-page pattern: concept, feature-state banner, then manifests and commands.
- Deprecated features (presets, OpenShift templates, Hook Sidecar) are labeled and link to replacements.
- Per-architecture (Arm64) device and feature-gate status pages.
- Deep, multi-level debugging content for advanced users.

Weaknesses:

- No end-to-end getting-started path inside the guide; the happy path is spread across five pages and external labs.
- Basic Use and Lifecycle are dated and VMI-centric, contradicting the VirtualMachine-first guidance elsewhere.
- No consolidated `virtctl` command reference or feature-gate table.
- No FAQ or user-facing troubleshooting page.
- Several v1.9 features (VirtualMachineBackup, CrossArchitectureVirtualization, PortRanges, migration compression) appear only in release notes; the Plugins page is orphaned from navigation.
- Compute and Storage sections are flat lists with API-style names and no landing page.
- Legacy installation content (OKD Service Catalog APB, k3OS, OpenShift 4.10 links) and a duplicate Windows virtio drivers page remain.

Rating: 3 - Meets standards
