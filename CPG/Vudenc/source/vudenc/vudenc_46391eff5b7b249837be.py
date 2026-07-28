"""Bot interface used in bot_config.py."""
import logging
import os
import threading
import time
import os_utilities
from utils import zip_package
THIS_FILE = os.path.abspath(zip_package.get_main_script_path())
def __init__(self, remote, attributes, server, server_version, base_dir,...
self._attributes = attributes
self._base_dir = base_dir
self._remote = remote
self._server = server
self._server_version = server_version
self._shutdown_hook = shutdown_hook
self._timers = []
self._timers_dying = False
self._timers_lock = threading.Lock()
@property...
"""docstring"""
return self._base_dir
