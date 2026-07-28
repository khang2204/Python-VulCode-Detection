"""
This module contains ...
"""
from __future__ import division, absolute_import
import cPickle as pickle
import pickle
import os
import time
import fnmatch
import hashlib
import re
import stat
import errno
from twisted.python import log
from cowrie.core.config import CONFIG
PICKLE = pickle.load(open(CONFIG.get('honeypot', 'filesystem_file'), 'rb'))
(A_NAME, A_TYPE, A_UID, A_GID, A_SIZE, A_MODE, A_CTIME, A_CONTENTS,
    A_TARGET, A_REALFILE) = list(range(0, 10))
T_LINK, T_DIR, T_FILE, T_BLK, T_CHR, T_SOCK, T_FIFO = list(range(0, 7))
"""
    62 ELOOP Too many levels of symbolic links.  A path name lookup involved more than 8 symbolic links.
    raise OSError(errno.ELOOP, os.strerror(errno.ENOENT))
    """
"""
    raise OSError(errno.ENOENT, os.strerror(errno.ENOENT))
    """
"""
    """
def __init__(self, fs, cfg):...
self.fs = fs
self.cfg = cfg
self.tempfiles = {}
self.filenames = {}
self.newcount = 0
self.init_honeyfs(self.cfg.get('honeypot', 'contents_path'))
def init_honeyfs(self, honeyfs_path):...
"""docstring"""
for path, directories, filenames in os.walk(honeyfs_path):
for filename in filenames:
def resolve_path(self, path, cwd):...
realfile_path = os.path.join(path, filename)
"""docstring"""
virtual_path = '/' + os.path.relpath(realfile_path, honeyfs_path)
pieces = path.rstrip('/').split('/')
f = self.getfile(virtual_path, follow_symlinks=False)
if path[0] == '/':
if f and f[A_TYPE] == T_FILE:
cwd = []
cwd = [x for x in cwd.split('/') if len(x) and x is not None]
self.update_realfile(f, realfile_path)
while 1:
if not len(pieces):
piece = pieces.pop(0)
return '/%s' % ('/'.join(cwd),)
if piece == '..':
if len(cwd):
if piece in ('.', ''):
cwd.pop()
cwd.append(piece)
