def UpdateDiagnosticInterface(self):...
if not self.DiagnosticsForCurrentFileReady():
return
self._diag_interface.UpdateWithNewDiagnostics(self.
    GetDiagnosticsFromStoredRequest())
