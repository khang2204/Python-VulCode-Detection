import os
import vim
import tempfile
import json
import signal
from subprocess import PIPE
from ycm import vimsupport
from ycm import utils
from ycm.diagnostic_interface import DiagnosticInterface
from ycm.completers.all.omni_completer import OmniCompleter
from ycm.completers.general import syntax_parse
from ycm.completers.completer_utils import FiletypeCompleterExistsForFiletype
from ycm.client.ycmd_keepalive import YcmdKeepalive
from ycm.client.base_request import BaseRequest, BuildRequestData
from ycm.client.command_request import SendCommandRequest
from ycm.client.completion_request import CompletionRequest
from ycm.client.omni_completion_request import OmniCompletionRequest
from ycm.client.event_notification import SendEventNotificationAsync, EventNotification
from ycm.server.responses import ServerError
from UltiSnips import UltiSnips_Manager
USE_ULTISNIPS_DATA = False
os.environ['no_proxy'] = '127.0.0.1,localhost'
USE_ULTISNIPS_DATA = True
signal.signal(signal.SIGINT, signal.SIG_IGN)
NUM_YCMD_STDERR_LINES_ON_CRASH = 30
SERVER_CRASH_MESSAGE_STDERR_FILE = (
    'The ycmd server SHUT DOWN (restart with :YcmRestartServer). ' +
    """Stderr (last {0} lines):

""".format(NUM_YCMD_STDERR_LINES_ON_CRASH))
SERVER_CRASH_MESSAGE_SAME_STDERR = (
    'The ycmd server SHUT DOWN (restart with :YcmRestartServer).  check console output for logs!'
    )
SERVER_IDLE_SUICIDE_SECONDS = 10800
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
def _IsServerAlive(self):...
args.append('--stderr={0}'.format(self._server_stderr))
returncode = self._server_popen.poll()
if self._user_options['server_keep_logfiles']:
return returncode is None
args.append('--keep_logfiles')
