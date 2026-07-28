def _load_ref_into_repo(self, fs_repo_root, branch, ref, without_timestamps...
"""docstring"""
metadata = self.read_metadata(ref)
added, removed, modified = self.workspace_changes(fs_repo_root, metadata,
    update_meta=False)
mfs_refpath, _ = refpath_to_mfs(Path(f'@{ref}'))
for path in added:
os.remove(path)
for path in (removed | modified):
mfs_path = self.get_mfs_path(fs_repo_root, branch, branch_info=mfs_refpath /
    path.relative_to(fs_repo_root))
timestamp = metadata[str(path)]['timestamp']
f.write(self.ipfs.files_read(mfs_path))
os.utime(path, ns=(timestamp, timestamp))
