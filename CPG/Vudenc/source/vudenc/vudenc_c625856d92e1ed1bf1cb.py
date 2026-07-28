from __future__ import absolute_import
import os
import traceback
import warnings
from ptvsd.socket import Address
from ptvsd._util import new_hidden_thread, Closeable, ClosedError
from .debugadapter import DebugAdapter, wait_for_socket_server
from .debugsession import DebugSession
SESSION = DebugSession
def __init__(self, addr=None, port=8888, breakpoints=None, connecttimeout=1.0):...
super(_LifecycleClient, self).__init__()
self._addr = Address.from_raw(addr, defaultport=port)
self._connecttimeout = connecttimeout
self._adapter = None
self._session = None
self._breakpoints = breakpoints
@property...
return self._adapter
