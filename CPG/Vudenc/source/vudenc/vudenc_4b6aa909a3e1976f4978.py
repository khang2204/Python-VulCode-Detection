def OnBufferUnload(self, deleted_buffer_file):...
if not self._IsServerAlive():
return
SendEventNotificationAsync('BufferUnload', {'unloaded_buffer':
    deleted_buffer_file})
