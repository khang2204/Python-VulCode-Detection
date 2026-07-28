def OnCurrentIdentifierFinished(self):...
if not self._IsServerAlive():
return
SendEventNotificationAsync('CurrentIdentifierFinished')
