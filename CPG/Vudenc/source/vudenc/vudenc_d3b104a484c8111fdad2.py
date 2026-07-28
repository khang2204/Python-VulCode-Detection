def GetDiagnosticsFromStoredRequest(self, qflist_format=False):...
if self.DiagnosticsForCurrentFileReady():
diagnostics = self._latest_file_parse_request.Response()
return []
self._latest_file_parse_request = None
if qflist_format:
return vimsupport.ConvertDiagnosticsToQfList(diagnostics)
return diagnostics
