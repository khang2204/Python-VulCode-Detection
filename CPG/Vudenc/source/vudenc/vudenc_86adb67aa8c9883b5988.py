def ShowDetailedDiagnostic(self):...
if not self._IsServerAlive():
return
debug_info = BaseRequest.PostDataToHandler(BuildRequestData(),
    'detailed_diagnostic')
vimsupport.PostVimMessage(str(e))
if 'message' in debug_info:
vimsupport.EchoText(debug_info['message'])
