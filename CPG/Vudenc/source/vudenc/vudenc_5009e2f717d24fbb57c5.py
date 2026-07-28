def reload(self):...
"""docstring"""
user = {}
mread = {}
mwrite = {}
mount = {}
if self.args.a:
for u, p in [x.split(':', 1) for x in self.args.a]:
if self.args.v:
user[u] = p
for src, dst, perms in [x.split(':', 2) for x in self.args.v]:
if self.args.c:
src = os.path.abspath(src)
for cfg_fn in self.args.c:
if not mount:
dst = dst.strip('/')
self._parse_config_file(f, user, mread, mwrite, mount)
vfs = VFS(os.path.abspath('.'), '', ['*'], ['*'])
if not '' in mount:
mount[dst] = src
maxdepth = 0
vfs = VFS(os.path.abspath('.'), '', [], [])
mread[dst] = []
for dst in sorted(mount.keys(), key=lambda x: (x.count('/'), len(x))):
mwrite[dst] = []
depth = dst.count('/')
self.vfs = vfs
perms = perms.split(':')
assert maxdepth <= depth
self.user = user
for lvl, uname in [[x[0], x[1:]] for x in perms]:
maxdepth = depth
self.iuser = self.invert(user)
if uname == '':
if dst == '':
uname = '*'
if lvl in 'ra':
vfs = VFS(mount[dst], dst, mread[dst], mwrite[dst])
v = vfs.add(mount[dst], dst)
mread[dst].append(uname)
if lvl in 'wa':
v.uread = mread[dst]
mwrite[dst].append(uname)
v.uwrite = mwrite[dst]
