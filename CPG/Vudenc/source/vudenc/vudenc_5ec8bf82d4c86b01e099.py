def RestartServer(self):...
vimsupport.PostVimMessage('Restarting ycmd server...')
self._user_notified_about_crash = False
self._ServerCleanup()
self._SetupServer()
