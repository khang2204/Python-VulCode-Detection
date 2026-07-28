def OnFileReadyToParse(self):...
self._omnicomp.OnFileReadyToParse(None)
if not self._IsServerAlive():
self._NotifyUserIfServerCrashed()
extra_data = {}
self._AddTagsFilesIfNeeded(extra_data)
self._AddSyntaxDataIfNeeded(extra_data)
self._AddExtraConfDataIfNeeded(extra_data)
self._latest_file_parse_request = EventNotification('FileReadyToParse',
    extra_data)
self._latest_file_parse_request.Start()
