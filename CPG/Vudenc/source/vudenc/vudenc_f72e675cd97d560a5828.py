def OnInsertLeave(self):...
if not self._IsServerAlive():
return
SendEventNotificationAsync('InsertLeave')
