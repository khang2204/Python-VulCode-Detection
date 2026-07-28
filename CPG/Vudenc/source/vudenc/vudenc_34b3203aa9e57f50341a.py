def getDistanceMatrix(self):...
"""docstring"""
Log.add('Calculating distance matrix in higher-order network (k = ' + str(
    self.order) + ') ...', Severity.INFO)
dist = _co.defaultdict(lambda : _co.defaultdict(lambda : _np.inf))
for v in self.nodes:
dist[v][v] = 0
for e in self.edges:
dist[e[0]][e[1]] = 1
for k in self.nodes:
for v in self.nodes:
Log.add('finished.', Severity.INFO)
for w in self.nodes:
return dist
if dist[v][w] > dist[v][k] + dist[k][w]:
dist[v][w] = dist[v][k] + dist[k][w]
