import os
import sys
import json
import shlex
from subprocess import PIPE
from process import spawn
from .error import AnaGondaError
from .base import AnaGondaContext
_go_get = 'gopkg.in/alecthomas/gometalinter.v1'
"""Fires on GometaLinter errors
    """
"""Context to run gometalinter tool into anaconda_go
    """
def __init__(self, options, filepath, env_ctx):...
self.filepath = filepath
self.options = options
super(GometaLinter, self).__init__(env_ctx, _go_get)
def __enter__(self):...
"""docstring"""
if self._bin_found is None:
if not os.path.exists(self.binary):
if not self._bin_found:
self._bin_found = True
self.go_get()
self._bin_found = False
return self.gometalinter()
self._install_linters()
