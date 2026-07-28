def update_size(self, filename, size):...
"""docstring"""
f = self.getfile(filename)
if f == False:
return
if f[A_TYPE] != T_FILE:
return
f[A_SIZE] = size
