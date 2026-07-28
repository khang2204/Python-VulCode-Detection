def list(self, keyfilter='/'):...
path = os.path.join(self.namespace, keyfilter)
if path != '/':
path = path.rstrip('/')
result = self.etcd.read(path, recursive=True)
return None
value = set()
for entry in result.get_subtree():
if entry.key == path:
return sorted(value)
name = entry.key[len(path):]
if entry.dir and not name.endswith('/'):
name += '/'
value.add(name.lstrip('/'))
