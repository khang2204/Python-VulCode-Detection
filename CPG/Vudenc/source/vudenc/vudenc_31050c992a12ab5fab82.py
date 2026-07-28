def ls(self, vpath, user):...
"""docstring"""
vn, rem = self._find(vpath)
if user not in vn.uread:
return [[], []]
rp = vn.realpath
if rem:
rp += '/' + rem
real = os.listdir(rp)
real.sort()
if rem:
virt_vis = []
virt_all = []
absreal = []
virt_vis = []
for p in real:
for name, vn2 in sorted(vn.nodes.items()):
absreal.append('{}/{}'.format(rp, p).replace('//', '/'))
return [absreal, virt_vis]
virt_all.append(name)
for name in virt_all:
if user in vn2.uread:
real.remove(name)
virt_vis.append(name)
