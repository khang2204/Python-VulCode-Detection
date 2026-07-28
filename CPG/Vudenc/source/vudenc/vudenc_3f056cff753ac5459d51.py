import os
import sys
import contextlib
import enum
from enum import Enum
def main():...
sh = Shell()
sh.run()
"""
    The main shell class.
    """
def __init__(self):...
self.builtins = {'exit': self._builtin_exit, 'pwd': self._builtin_pwd, 'cd':
    self._builtin_cd}
def run(self):...
"""docstring"""
while True:
line = self.readline()
sys.exit(0)
self.execute(line)
