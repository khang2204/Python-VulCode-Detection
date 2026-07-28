"""
Set user settings to optimize performance, Finder and windowing features, and automate standard preference
settings.

While this is an Apple specific script, it doesn't check to see if it's executing on a Mac.
"""
import dglogger
import argparse
import os
import getpass
import grp
import platform
import re
import pexpect
import shlex
import subprocess
import sys
def is_admin():...
"""docstring"""
return os.getlogin() in grp.getgrnam('admin').gr_mem
