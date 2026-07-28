def updateCacheID(self, pth, cacheID):...
"""docstring"""
command = "UPDATE {0} SET file_id='{1}' WHERE path='{2}'".format(TABLE_NAME,
    cacheID, pth)
self._run_command(command)
