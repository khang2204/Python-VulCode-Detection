def getFileCacheID(self, pth):...
"""docstring"""
command = "SELECT file_id FROM {0} WHERE path='{1}'".format(TABLE_NAME, pth)
data = self._run_command(command)
data = data[0][0]
data = None
return data
