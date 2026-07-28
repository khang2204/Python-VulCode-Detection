"""Runs a Swarming task.

Downloads all the necessary files to run the task, executes the command and
streams results back to the Swarming server.

The process exit code is 0 when the task was executed, even if the task itself
failed. If there's any failure in the setup or teardown, like invalid packet
response, failure to contact the server, etc, a non zero exit code is used. It's
up to the calling process (bot_main.py) to signal that there was an internal
failure and to cancel this task run and ask the server to retry it.
"""
import base64
import json
import logging
import optparse
import os
import signal
import sys
import time
import xsrf_client
from utils import net
from utils import on_error
from utils import subprocess42
from utils import zip_package
THIS_FILE = os.path.abspath(zip_package.get_main_script_path())
MAX_CHUNK_SIZE = 102400
MAX_PACKET_INTERVAL = 30
MIN_PACKET_INTERNAL = 10
OUT_VERSION = 3
SIG_BREAK_OR_TERM = (signal.SIGBREAK if sys.platform == 'win32' else signal
    .SIGTERM)
_last_now = 0
def monotonic_time():...
"""docstring"""
now = time.time()
if now > _last_now:
_last_now = now
return _last_now
