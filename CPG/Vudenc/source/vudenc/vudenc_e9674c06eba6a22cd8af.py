def getAdjacencyMatrix(self, includeSubPaths=True, weighted=True,...
"""docstring"""
row = []
col = []
data = []
if transposed:
for s, t in self.edges:
for s, t in self.edges:
row.append(self.nodes.index(t))
if not weighted:
row.append(self.nodes.index(s))
col.append(self.nodes.index(s))
data = _np.ones(len(self.edges.keys()))
if includeSubPaths:
col.append(self.nodes.index(t))
return _sparse.coo_matrix((data, (row, col)), shape=(self.vcount(), self.
    vcount())).tocsr()
data = _np.array([float(x.sum()) for x in self.edges.values()])
data = _np.array([float(x[1]) for x in self.edges.values()])
