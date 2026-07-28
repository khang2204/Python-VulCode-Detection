def __init__(self, user_options):...
self._user_options = user_options
self._user_notified_about_crash = False
self._diag_interface = DiagnosticInterface(user_options)
self._omnicomp = OmniCompleter(user_options)
self._latest_completion_request = None
self._latest_file_parse_request = None
self._server_stdout = None
self._server_stderr = None
self._server_popen = None
self._filetypes_with_keywords_loaded = set()
self._temp_options_filename = None
self._ycmd_keepalive = YcmdKeepalive()
self._SetupServer()
self._ycmd_keepalive.Start()
