def totalEdgeWeight(self):...
"""docstring"""
if self.edges:
return sum(self.edges.values())
return _np.array([0, 0])
