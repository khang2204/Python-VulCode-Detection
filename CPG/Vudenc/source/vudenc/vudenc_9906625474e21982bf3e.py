def findObjects(origin):...
"""docstring"""
traverse = origin.unrestrictedTraverse
base = '/'.join(origin.getPhysicalPath())
if isinstance(base, six.text_type):
base = base.encode('utf-8')
cut = len(base) + 1
paths = [base]
for idx, path in enumerate(paths):
obj = traverse(path)
yield path[cut:], obj
if hasattr(aq_base(obj), 'objectIds'):
for id in obj.objectIds():
if isinstance(id, six.text_type):
id = id.encode('utf-8')
paths.insert(idx + 1, path + b'/' + id)
