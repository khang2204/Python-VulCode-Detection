def isdir(self, path):...
"""docstring"""
if path == '/':
return True
dir = self.getfile(path)
dir = None
if dir is None or dir is False:
return False
if dir[A_TYPE] == T_DIR:
return True
return False
