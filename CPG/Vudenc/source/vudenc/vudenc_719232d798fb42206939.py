def getFileList(self):...
"""docstring"""
command = 'SELECT path FROM {0};'.format(TABLE_NAME)
data = self._run_command(command)
data = [i[0] for i in data]
data = None
return data
