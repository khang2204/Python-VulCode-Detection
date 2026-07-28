def updateModTime(self, pth, mod_time):...
"""docstring"""
if self.fileExists(pth):
command = "UPDATE {0} SET mod_time={1} WHERE path='{2}';".format(TABLE_NAME,
    mod_time, pth)
print("updateModTime: file doesn't exist!")
self._run_command(command)
