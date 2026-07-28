from builtins import str
import logging
import random
import socket
import subprocess
import time
"""Raised when there is an error in adb operations."""
def __init__(self, cmd, stdout, stderr, ret_code):...
self.cmd = cmd
self.stdout = stdout
self.stderr = stderr
self.ret_code = ret_code
def __str__(self):...
return 'Error executing adb cmd "%s". ret: %d, stdout: %s, stderr: %s' % (self
    .cmd, self.ret_code, self.stdout, self.stderr)
