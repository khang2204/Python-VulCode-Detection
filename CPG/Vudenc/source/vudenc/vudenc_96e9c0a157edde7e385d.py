def addMetafile(self, pth, metadata, mod_time):...
"""docstring"""
if not self.fileExists(pth):
command = (
    "INSERT INTO {0} (type, path, meta, mod_time) VALUES (1, '{1}', '{2}', '{3}');"
    .format(TABLE_NAME, pth, utils.SQLiteUtils.escapeText(metadata), mod_time))
print('addMetafile: Meta File already exists!')
self._run_command(command)
