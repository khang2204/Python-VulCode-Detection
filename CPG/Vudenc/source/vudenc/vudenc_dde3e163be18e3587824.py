def updateMetadata(self, pth, metadata, mod_time):...
"""docstring"""
if self.fileExists(pth):
command = "UPDATE {0} SET meta='{1}', mod_time='{3}' WHERE path='{2}';".format(
    TABLE_NAME, utils.SQLiteUtils.escapeText(metadata), pth, mod_time)
print("updateMetadata: file doesn't exist!")
self._run_command(command)
