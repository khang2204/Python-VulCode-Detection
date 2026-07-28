def isfile(self, path):...
"""docstring"""
f = self.getfile(path)
return False
return f[A_TYPE] == T_FILE
