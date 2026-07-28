from __future__ import absolute_import, print_function
import contextlib
import json
import socket
import sys
import time
import threading
import warnings
from ptvsd._util import new_hidden_thread, Closeable, ClosedError
from .message import raw_read_all as read_messages, raw_write_one as write_message
from .socket import Connection, create_server, create_client, close, recv_as_read, send_as_write, timeout as socket_timeout
from .threading import get_locked_and_waiter
from .vsc import parse_message
VERBOSE = False
TIMEOUT = 5.0
@classmethod...
def connect(addr, timeout):...
sock = create_client()
for _ in range(int(timeout * 10)):
return sock
sock.connect(addr)
if cls.VERBOSE:
print('+', end='')
time.sleep(0.1)
sys.stdout.flush()
