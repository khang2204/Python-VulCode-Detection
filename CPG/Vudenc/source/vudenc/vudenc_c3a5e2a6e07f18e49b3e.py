def _SetupServer(self):...
server_port = utils.GetUnusedLocalhostPort()
self._temp_options_filename = options_file.name
json.dump(dict(self._user_options), options_file)
options_file.flush()
args = [utils.PathToPythonInterpreter(), _PathToServerScript(),
    '--port={0}'.format(server_port), '--options_file={0}'.format(
    options_file.name), '--log={0}'.format(self._user_options[
    'server_log_level']), '--idle_suicide_seconds={0}'.format(
    SERVER_IDLE_SUICIDE_SECONDS)]
if not self._user_options['server_use_vim_stdout']:
filename_format = os.path.join(utils.PathToTempDir(), 'server_{port}_{std}.log'
    )
self._server_popen = utils.SafePopen(args, stdout=PIPE, stderr=PIPE)
self._server_stdout = filename_format.format(port=server_port, std='stdout')
BaseRequest.server_location = 'http://localhost:' + str(server_port)
self._server_stderr = filename_format.format(port=server_port, std='stderr')
self._NotifyUserIfServerCrashed()
args.append('--stdout={0}'.format(self._server_stdout))
args.append('--stderr={0}'.format(self._server_stderr))
if self._user_options['server_keep_logfiles']:
args.append('--keep_logfiles')
