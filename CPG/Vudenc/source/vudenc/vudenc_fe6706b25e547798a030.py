def HigherOrderPathToFirstOrder(self, path):...
"""docstring"""
p1 = self.HigherOrderNodeToPath(path[0])
for x in path[1:]:
p1 += self.HigherOrderNodeToPath(x)[-1],
return p1
