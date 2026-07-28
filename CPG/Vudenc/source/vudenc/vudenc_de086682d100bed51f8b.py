def traverse_path(obj, path):...
"""docstring"""
if not path or path == '/':
return [obj], []
path = re.sub('\\/+', '/', path)
if path.endswith('/'):
path = path[:-1]
if path.startswith('/'):
path = path[1:]
path = path.split('/')
ret = [obj]
while path:
name = path[0]
return ret[1:], path
traverser = ITraverser(ret[-1])
next_obj = follow_symlinks(traverser.traverse(name))
if not next_obj:
ret.append(next_obj)
path = path[1:]
