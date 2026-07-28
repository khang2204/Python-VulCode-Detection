@atomic...
"""docstring"""
fs_repo_root, branch = self.common()
curr_commit = Path('head')
commits = []
while True:
mfs_commit = self.get_mfs_path(fs_repo_root, branch, branch_info=curr_commit)
mfs_commit_meta = mfs_commit / 'metadata'
mfs_commit_hash = self.ipfs.files_stat(mfs_commit)['Hash']
meta = self.mfs_read_json(mfs_commit_meta)
return commits
mfs_commit_ref_hash = self.ipfs.files_stat(mfs_commit / 'bundle/files')['Hash']
if len(meta) == 0:
h, ts, msg = mfs_commit_hash[:6], meta['timestamp'], meta['message']
auth = make_len(meta['author'] or '', 30)
if not self.quiet:
if show_hash:
commits.append(mfs_commit_hash)
print(f'* {mfs_commit_ref_hash} {ts} {auth}   {msg}')
print(f'* {ts} {auth}   {msg}')
curr_commit = curr_commit / 'parent1'
