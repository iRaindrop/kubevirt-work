# KubeVirt inclusive language: recommendations

The following recommendations address the inclusive language of the KubeVirt user guide.

- Remove or reword minimizing language across the guide. Delete "simply", "just", "of course", and "obviously" where they add nothing, and replace "easy" or "easily" with a concrete statement of what the step requires (for example, change "can be easily cancelled" to "can be cancelled by deleting the migration object"). Start with the pages that have the most occurrences: Live Migration, Windows Virtio Drivers, Node Assignment, vsock, and Disks and Volumes.
- Add a rule to the documentation style guide (see the content creation process recommendations) that discourages "simple", "simply", "easy", "easily", "just", and "obviously", with a one-line explanation of why.
- Add an automated check for minimizing and non-recommended language to the Makefile and the Prow presubmit, using a tool such as Vale with the `alex` or `write-good` style, or a grep-based check alongside `make check_spelling`, so new occurrences are flagged in pull requests.
- Update the 14 links to `kubevirt.io/api-reference/master/...` to the `/main/` path, or to a specific version path such as `/v1.9.0/`, so the guide no longer points at a legacy branch name.
- Replace the `kubevirt.io/nodeName: master` example on the Presets page with a neutral node name such as `node01`, or remove the example, since the page documents a deprecated feature.
- Ask the KubeVirt API maintainers whether the `Abort Requested` and `Abort Status` fields in the VirtualMachineInstanceMigration status are candidates for a "cancel" alias in a future API version; until then, prefer "cancel" in the prose of the Live Migration page while continuing to show the field names as they appear in `kubectl` output.
- When upstream projects linked from the guide (libvirt, cri-tools, vhostmd, kubevirt-ansible) rename their default branch, update the links; in the meantime prefer tagged or permalink URLs so the branch name is not repeated in the guide.
