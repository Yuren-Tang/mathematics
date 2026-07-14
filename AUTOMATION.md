# Automatic public chronology

A push to `main` that changes `projects/**` or `unfiled/**` triggers the
timestamp workflow.

For every new commit in that push that changes public mathematical material,
the workflow creates a canonical manifest containing:

- repository name;
- commit, tree and parent hashes;
- changed paths and change types;
- Git blob IDs;
- SHA-256 hashes and byte lengths of the exact file contents.

The manifest is submitted to OpenTimestamps. The manifest and `.ots` proof are
stored on the separate `attestations` branch. A scheduled workflow upgrades
pending proofs.

The manifest is determined by the commit itself, so rerunning the workflow does
not create a different record.

## One-time GitHub setting

The workflow requests `contents: write`. If repository policy overrides that
permission, enable:

**Settings → Actions → General → Workflow permissions → Read and write
permissions**

The main mathematical branch should not normally be force-pushed.
