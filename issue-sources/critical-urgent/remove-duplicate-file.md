<!-- Make sure that you visit our User Guide at https://kubevirt.io/user-guide.
-->

**Description**:
Delete `docs/compute/windows_virtio_drivers.md`, which is a byte-identical duplicate of `docs/user_workloads/windows_virtio_drivers.md` and is not listed in any `.nav.yml`. If the `compute/windows_virtio_drivers/` URL was ever published, add a redirect to `user_workloads/windows_virtio_drivers/` in the `redirects` plugin section of `mkdocs.yml`.

**What you expected**:
Each topic exists in exactly one file, and any previously published URL still resolves.

**URL**:
`docs/compute/windows_virtio_drivers.md`

**Additional context**:
Repository maintenance.
