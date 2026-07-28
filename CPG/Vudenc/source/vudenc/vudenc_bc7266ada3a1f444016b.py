def getDistanceMatrixFirstOrder(self):...
"""docstring"""
dist = self.getDistanceMatrix()
dist_first = _co.defaultdict(lambda : _co.defaultdict(lambda : _np.inf))
for vk in dist:
for wk in dist[vk]:
return dist_first
v1 = self.HigherOrderNodeToPath(vk)[0]
w1 = self.HigherOrderNodeToPath(wk)[-1]
if dist[vk][wk] + self.order - 1 < dist_first[v1][w1]:
dist_first[v1][w1] = dist[vk][wk] + self.order - 1
