def validate_deps(graph):...
"""docstring"""
test_graph = {}
for case, deps in graph.items():
test_deps = [d.check.name for d in deps]
visited = set()
test_graph[case.check.name] += test_deps
test_graph[case.check.name] = test_deps
unvisited = list(itertools.zip_longest(test_graph.keys(), [], fillvalue=None))
path = []
while unvisited:
node, parent = unvisited.pop()
while path and path[-1] != parent:
path.pop()
adjacent = reversed(test_graph[node])
path.append(node)
for n in adjacent:
if n in path:
visited.add(node)
cycle_str = '->'.join(path + [n])
if n not in visited:
unvisited.append((n, node))
