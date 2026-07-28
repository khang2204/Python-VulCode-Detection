@atomic...
_, branch = self.common()
if not name.replace('_', '').isalnum():
if not self.quiet:
if name in ['head', 'workspace', 'stage']:
print('Branch name has to be alpha numeric with underscores', file=sys.stderr)
self.ipfs.files_stat(self.get_mfs_path(self.fs_cwd, name))
if from_commit == '@head':
if not self.quiet:
if not self.quiet:
self.ipfs.files_cp(self.get_mfs_path(self.fs_cwd, branch), self.
    get_mfs_path(self.fs_cwd, name))
for ref in ['stage', 'workspace']:
print(f'"{name}" is a reserved keyword, please pick a different branch name',
    file=sys.stderr)
print('Branch name already exists', file=sys.stderr)
if not no_checkout:
mfs_ref = self.get_mfs_path(self.fs_cwd, name, branch_info=ref)
commit_path = expand_ref(from_commit)
self.checkout(name)
self.ipfs.files_mkdir(mfs_ref, parents=True)
mfs_commit_path = self.get_mfs_path(self.fs_cwd, branch, branch_info=
    commit_path)
mfs_head_path = self.get_mfs_path(self.fs_cwd, name, branch_info='head')
self.ipfs.files_stat(mfs_commit_path)
if not self.quiet:
self.ipfs.files_cp(mfs_commit_path, mfs_head_path)
print('No such commit', file=sys.stderr)
mfs_commit_bundle_path = f'{mfs_commit_path}/bundle'
mfs_workspace_path = self.get_mfs_path(self.fs_cwd, name, branch_info=
    'workspace/bundle')
mfs_stage_path = self.get_mfs_path(self.fs_cwd, name, branch_info=
    'stage/bundle')
self.ipfs.files_cp(mfs_commit_bundle_path, mfs_workspace_path)
self.ipfs.files_cp(mfs_commit_bundle_path, mfs_stage_path)
