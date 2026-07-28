def undot(self, path):...
ret = []
for node in path.split('/'):
if node in ['', '.']:
return '/'.join(ret)
if node == '..':
if ret:
ret.append(node)
ret.pop()
