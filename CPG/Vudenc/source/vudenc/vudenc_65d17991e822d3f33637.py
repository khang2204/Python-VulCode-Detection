@atomic...
"""docstring"""
fs_repo_root, _ = self.common()
self.ipfs.files_stat(self.get_mfs_path(self.fs_cwd, name))
if not self.quiet:
self.ipfs.files_write(self.get_mfs_path(self.fs_cwd, repo_info=
    'active_branch_name'), io.BytesIO(bytes(name, 'utf-8')), create=True,
    truncate=True)
print('No branch by that name exists', file=sys.stderr)
self._load_ref_into_repo(fs_repo_root, name, 'workspace', without_timestamps)
