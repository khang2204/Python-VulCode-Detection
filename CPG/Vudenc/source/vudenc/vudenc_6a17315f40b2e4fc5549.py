def periodicRoutine(self):...
"""docstring"""
if not hasattr(self, 'update_filelist_thread_queue'):
self.update_filelist_thread_queue = Queue()
while not self.update_filelist_thread_queue.empty():
q = self.update_filelist_thread_queue.get()
self.updateFileListThread()
self.last_filelist_update_time = q[0]
for user in self.userparams.getAllEntries(fields=['subscribed', 'period',
if user[0] == 1:
cur_time = time()
if cur_time - user[2] > user[1]:
self.startRandomPicThread(user[3], MMKM=getMainMenu(True))
self.userparams.setEntry(user[3], 'last_update_time', cur_time)
