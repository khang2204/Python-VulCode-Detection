@atomic...
_, branch = self.common()
active = self.ipfs.files_read(self.get_mfs_path(self.fs_cwd, repo_info=
    'active_branch_name')).decode('utf-8')
if not self.quiet:
print(active)
return active
