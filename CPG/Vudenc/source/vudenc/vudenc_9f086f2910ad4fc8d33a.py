def addFile(self, pth, mod_time=None):...
"""docstring"""
if not self.fileExists(pth):
if not mod_time:
print('addFile: File already exists!')
mod_time = utils.FileUtils.getModificationTimeUnix(pth)
command = ("INSERT INTO {0} (type, path, mod_time) VALUES (0, '{1}', {2});"
    .format(TABLE_NAME, pth, mod_time))
self._run_command(command)
