@atomic...
"""docstring"""
mfs_commit_hash = self.get_refpath_hash(refpath)
if browser:
url = f'http://localhost:8080/ipfs/{mfs_commit_hash}'
ret = self.ipfs.ls(f'/ipfs/{mfs_commit_hash}')
if not self.quiet:
obj = ret['Objects'][0]
print(f'Opening {url}')
webbrowser.open(url)
if len(obj['Links']) == 0:
cat = self.ipfs.cat(f'/ipfs/{mfs_commit_hash}').decode('utf-8')
ls = '\n'.join([ln['Name'] for ln in obj['Links']])
if not self.quiet:
if not self.quiet:
print(cat)
return cat
print(ls)
return ls
