def updateFileListThread(self):...
"""docstring"""
if not hasattr(self, 'last_filelist_update_time') or time(
if not (hasattr(self, 'filelist_updater_thread') and self.
self.filelist_updater_thread = Thread(target=self.updateFileList)
print('updater already running!')
self.filelist_updater_thread.start()
