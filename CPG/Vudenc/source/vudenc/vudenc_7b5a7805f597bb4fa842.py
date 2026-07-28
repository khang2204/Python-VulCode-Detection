def getShortestPaths(self):...
"""docstring"""
Log.add('Calculating shortest paths in higher-order network (k = ' + str(
    self.order) + ') ...', Severity.INFO)
dist = _co.defaultdict(lambda : _co.defaultdict(lambda : _np.inf))
shortest_paths = _co.defaultdict(lambda : _co.defaultdict(lambda : set()))
for e in self.edges:
dist[e[0]][e[1]] = 1
for v in self.nodes:
shortest_paths[e[0]][e[1]].add(e)
for w in self.nodes:
for v in self.nodes:
if v != w:
dist[v][v] = 0
Log.add('finished.', Severity.INFO)
for k in self.nodes:
shortest_paths[v][v].add((v,))
return shortest_paths
if dist[v][w] > dist[v][k] + dist[k][w]:
dist[v][w] = dist[v][k] + dist[k][w]
if dist[v][w] == dist[v][k] + dist[k][w]:
shortest_paths[v][w] = set()
for p in list(shortest_paths[v][k]):
for p in list(shortest_paths[v][k]):
for q in list(shortest_paths[k][w]):
for q in list(shortest_paths[k][w]):
shortest_paths[v][w].add(p + q[1:])
shortest_paths[v][w].add(p + q[1:])
