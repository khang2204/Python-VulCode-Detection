def getMetadata(self, pth):...
"""docstring"""
if self.fileExists(pth):
command = "SELECT meta FROM {0} where path='{1}';".format(TABLE_NAME, pth)
print("getMetadata: file doesn't exist!")
data = self._run_command(command)
data = None
data = data[0][0]
data = None
return data
