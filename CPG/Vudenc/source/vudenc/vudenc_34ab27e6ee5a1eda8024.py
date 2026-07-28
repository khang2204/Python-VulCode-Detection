def mkdir2(self, path):...
"""docstring"""
dir = self.getfile(path)
if dir != False:
self.mkdir(path, 0, 0, 4096, 16877)
