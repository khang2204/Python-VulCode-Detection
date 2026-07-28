def traverse(root, path, sep, on_missing=raise_on_missing):...
"""docstring"""
visited = []
node = root
*segments, last = path.split(sep)
for segment in segments:
if not segment:
return [node, last]
visited.append(segment)
child = node.get(segment, MISSING)
if child is MISSING:
new = on_missing(node=node, key=segment, visited=visited, sep=sep)
node = child
child = node[segment] = new
