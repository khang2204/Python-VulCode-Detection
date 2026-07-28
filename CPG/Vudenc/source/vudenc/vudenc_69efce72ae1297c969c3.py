def GetDefinedSubcommands(self):...
if self._IsServerAlive():
return BaseRequest.PostDataToHandler(BuildRequestData(), 'defined_subcommands')
return []
