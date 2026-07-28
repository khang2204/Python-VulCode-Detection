def deleteFile(self, pth):...
"""docstring"""
command = "DELETE FROM {0} WHERE path='{1}';".format(TABLE_NAME, pth)
self._run_command(command)
