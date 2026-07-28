def invalidateCached(self, pth):...
"""docstring"""
command = "UPDATE {0} SET file_id=NULL WHERE path='{1}'".format(TABLE_NAME, pth
    )
self._run_command(command)
