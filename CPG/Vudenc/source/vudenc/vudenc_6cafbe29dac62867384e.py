def OnBufferVisit(self):...
if not self._IsServerAlive():
return
extra_data = {}
_AddUltiSnipsDataIfNeeded(extra_data)
SendEventNotificationAsync('BufferVisit', extra_data)
