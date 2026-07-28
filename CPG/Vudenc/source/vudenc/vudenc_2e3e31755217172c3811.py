def add(self, src, dst):...
"""docstring"""
assert not src.endswith('/')
assert not dst.endswith('/')
if '/' in dst:
name, dst = dst.split('/', 1)
if dst in self.nodes:
if name in self.nodes:
return self.nodes[dst]
vp = '{}/{}'.format(self.vpath, dst).lstrip('/')
return self.nodes[name].add(src, dst)
vn = VFS('{}/{}'.format(self.realpath, name), '{}/{}'.format(self.vpath,
    name).lstrip('/'), self.uread, self.uwrite)
vn = VFS(src, vp)
self.nodes[name] = vn
self.nodes[dst] = vn
return vn.add(src, dst)
return vn
