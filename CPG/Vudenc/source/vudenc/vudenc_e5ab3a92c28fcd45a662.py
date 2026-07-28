"""Base class for clients that communicate with apps over a JSON RPC interface.

The JSON protocol expected by this module is:

Request:
{
    "id": <monotonically increasing integer containing the ID of this request>
    "method": <string containing the name of the method to execute>
    "params": <JSON array containing the arguments to the method>
}

Response:
{
    "id": <int id of request that this response maps to>,
    "result": <Arbitrary JSON object containing the result of executing the
               method. If the method could not be executed or returned void,
               contains 'null'.>,
    "error": <String containing the error thrown by executing the method.
              If no error occurred, contains 'null'.>
    "callback": <String that represents a callback ID used to identify events
                 associated with a particular CallbackHandler object.>
"""
from builtins import str
import json
import logging
import socket
import threading
import time
from mobly.controllers.android_device_lib import adb
from mobly.controllers.android_device_lib import callback_handler
APP_START_WAIT_TIME = 15
UNKNOWN_UID = -1
_SOCKET_CONNECTION_TIMEOUT = 60
_SOCKET_READ_TIMEOUT = callback_handler.MAX_TIMEOUT
"""Raised when the app is not able to be started."""
"""Raised when remote API reports an error."""
"""Raised when there is some error in exchanging data with server."""
NO_RESPONSE_FROM_HANDSHAKE = 'No response from handshake.'
NO_RESPONSE_FROM_SERVER = 'No response from server.'
MISMATCHED_API_ID = 'Mismatched API id.'
"""Commands that can be invoked on all jsonrpc clients.

    INIT: Initializes a new session.
    CONTINUE: Creates a connection.
    """
INIT = 'initiate'
CONTINUE = 'continue'
"""Base class for jsonrpc clients that connect to remote servers.

    Connects to a remote device running a jsonrpc-compatible app. Before opening
    a connection a port forward must be setup to go over usb. This be done using
    adb.tcp_forward(). This calls the shell command adb forward <local> remote>.
    Once the port has been forwarded it can be used in this object as the port
    of communication.

    Attributes:
        host_port: (int) The host port of this RPC client.
        device_port: (int) The device port of this RPC client.
        app_name: (str) The user-visible name of the app being communicated
                  with.
        uid: (int) The uid of this session.
    """
def __init__(self, host_port, device_port, app_name, adb_proxy, log=logging...
"""docstring"""
self.host_port = host_port
self.device_port = device_port
self.app_name = app_name
self.uid = None
self._adb = adb_proxy
self._client = None
self._conn = None
self._counter = None
self._lock = threading.Lock()
self._event_client = None
self._log = log
def __del__(self):...
self.close()
def _do_start_app(self):...
"""docstring"""
def _start_event_client(self):...
"""docstring"""
def stop_app(self):...
"""docstring"""
def check_app_installed(self):...
"""docstring"""
def start_app(self, wait_time=APP_START_WAIT_TIME):...
"""docstring"""
self.check_app_installed()
self._do_start_app()
for _ in range(wait_time):
time.sleep(1)
def connect(self, uid=UNKNOWN_UID, cmd=JsonRpcCommand.INIT):...
if self._is_app_running():
"""docstring"""
self._log.debug('Successfully started %s', self.app_name)
self._counter = self._id_counter()
return
self._conn = socket.create_connection(('127.0.0.1', self.host_port),
    _SOCKET_CONNECTION_TIMEOUT)
self._conn.settimeout(_SOCKET_READ_TIMEOUT)
self._client = self._conn.makefile(mode='brw')
resp = self._cmd(cmd, uid)
if not resp:
result = json.loads(str(resp, encoding='utf8'))
if result['status']:
self.uid = result['uid']
self.uid = UNKNOWN_UID
def close(self):...
"""docstring"""
if self._conn:
self._conn.close()
def _adb_grep_wrapper(self, adb_shell_cmd):...
self._conn = None
"""docstring"""
return self._adb.shell(adb_shell_cmd).decode('utf-8')
if e.ret_code == 1 and not e.stdout and not e.stderr:
def _cmd(self, command, uid=None):...
return False
"""docstring"""
if not uid:
uid = self.uid
self._client.write(json.dumps({'cmd': command, 'uid': uid}).encode('utf8') +
    b'\n')
self._client.flush()
return self._client.readline()
