<!-- Make sure that you visit our User Guide at https://kubevirt.io/user-guide.
-->

**Description**:
Update the 14 links to `kubevirt.io/api-reference/master/...` so they point to the `/main/` path, or to a specific version path such as `/v1.9.0/`. The affected files are:

- `docs/cluster_admin/customize_components.md`
- `docs/cluster_admin/installation.md`
- `docs/cluster_admin/migration_policies.md`
- `docs/compute/virtual_hardware.md`
- `docs/debug_virt_stack/debug.md`
- `docs/network/interfaces_and_networks.md`
- `docs/storage/disks_and_volumes.md`

**What you expected**:
The guide no longer references the legacy `master` branch name in API reference links.

**URL**:
`docs/**/*.md` (see list above)

**Additional context**:
Inclusive language.
