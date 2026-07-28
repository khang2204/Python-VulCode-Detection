def pathToHigherOrderNodes(self, path, k=None):...
"""docstring"""
if k is None:
k = self.order
assert len(path) > k, 'Error: Path must be longer than k'
if k == 0 and len(path) == 1:
return ['start', path[0]]
return [self.separator.join(path[n:n + k]) for n in range(len(path) - k + 1)]
