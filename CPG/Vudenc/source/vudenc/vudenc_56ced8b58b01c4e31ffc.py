def chmod(self, path, perm):...
"""docstring"""
p = self.getfile(path)
if p == False:
p[A_MODE] = stat.S_IFMT(p[A_MODE]) | perm
