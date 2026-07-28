def getModTime(self, pth):...
"""docstring"""
if self.fileExists(pth):
command = "SELECT mod_time FROM {0} WHERE path='{1}';".format(TABLE_NAME, pth)
print("getModTime: File doesn't exist")
result = self._run_command(command)
result = None
result = result[0][0]
result = None
return result
