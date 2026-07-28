def getTransitionMatrix(self, includeSubPaths=True):...
"""docstring"""
row = []
col = []
data = []
if includeSubPaths:
D = [self.outweights[x].sum() for x in self.nodes]
D = [self.outweights[x][1] for x in self.nodes]
for s, t in self.edges:
if self.edges[s, t][1] > 0 or includeSubPaths and self.edges[s, t][0] > 0:
data = _np.array(data)
row.append(self.nodes.index(t))
data = data.reshape(data.size)
col.append(self.nodes.index(s))
return _sparse.coo_matrix((data, (row, col)), shape=(self.vcount(), self.
    vcount())).tocsr()
if includeSubPaths:
count = self.edges[s, t].sum()
count = self.edges[s, t][1]
assert D[self.nodes.index(s)
    ] > 0, 'Encountered zero out-degree for node ' + str(s
    ) + ' while weight of link (' + str(s) + ', ' + str(t) + ') is non-zero.'
prob = count / D[self.nodes.index(s)]
if prob < 0 or prob > 1:
tn.Log.add('Encountered transition probability outside [0,1] range.',
    Severity.ERROR)
data.append(prob)
