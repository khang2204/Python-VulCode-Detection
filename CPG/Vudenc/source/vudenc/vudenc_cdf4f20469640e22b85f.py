def _NotifyUserIfServerCrashed(self):...
if self._user_notified_about_crash or self._IsServerAlive():
return
self._user_notified_about_crash = True
if self._server_stderr:
error_output = ''.join(server_stderr_file.readlines()[:-
    NUM_YCMD_STDERR_LINES_ON_CRASH])
vimsupport.PostVimMessage(SERVER_CRASH_MESSAGE_SAME_STDERR)
vimsupport.PostMultiLineNotice(SERVER_CRASH_MESSAGE_STDERR_FILE + error_output)
