def getLaplacianMatrix(self, includeSubPaths=True):...
"""docstring"""
T = self.getTransitionMatrix(includeSubPaths)
I = _sparse.identity(self.vcount())
return I - T
