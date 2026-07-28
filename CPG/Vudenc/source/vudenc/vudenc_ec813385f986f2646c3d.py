def getIDbyPath(self, pth):...
"""docstring"""
command = "SELECT ID FROM {0} WHERE path='{1}';".format(TABLE_NAME, pth)
data = self._run_command(command)
result = data[0][0]
result = None
return result
