from __future__ import absolute_import
import logging
import os
import sys
import atexit
from lore import env, util, ansi
from lore.ansi import underline
from lore.util import timer
logger = logging.getLogger(__name__)
if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
ModuleNotFoundError = ImportError
__author__ = 'Montana Low and Jeremy Stanley'
__copyright__ = 'Copyright © 2017, Instacart'
__credits__ = ['Montana Low', 'Jeremy Stanley', 'Emmanuel Turlay']
__license__ = 'MIT'
__version__ = '0.4.45'
__maintainer__ = 'Montana Low'
__email__ = 'montana@instacart.com'
__status__ = 'Development Status :: 3 - Alpha'
def banner():...
import socket
import getpass
return '%s in %s on %s' % (ansi.foreground(ansi.GREEN, env.project), ansi.
    foreground(env.color, env.name), ansi.foreground(ansi.CYAN, getpass.
    getuser() + '@' + socket.gethostname()))
