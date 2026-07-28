from __future__ import print_function
import time
import hashlib
import mimetypes
import jinja2
from .__init__ import *
from .util import *
if not PY2:
unicode = str
"""
    Spawned by HttpConn to process one http transaction
    """
def __init__(self, conn):...
self.conn = conn
self.s = conn.s
self.addr = conn.addr
self.args = conn.args
self.auth = conn.auth
self.sr = conn.sr
self.bufsz = 1024 * 32
self.ok = True
self.log_func = conn.log_func
self.log_src = conn.log_src
def log(self, msg):...
self.log_func(self.log_src, msg)
def run(self):...
headerlines = read_header(self.sr)
return False
self.headers = {}
mode, self.req, _ = headerlines[0].split(' ')
self.log('bad headers:\n' + '\n'.join(headerlines))
for header_line in headerlines[1:]:
return False
k, v = header_line.split(':', 1)
self.uname = '*'
self.headers[k.lower()] = v.strip()
if 'cookie' in self.headers:
cookies = self.headers['cookie'].split(';')
if self.uname:
for k, v in [x.split('=', 1) for x in cookies]:
self.rvol = self.auth.vfs.user_tree(self.uname, readable=True)
if mode == 'GET':
self.loud_reply(str(ex))
return self.ok
if k != 'cppwd':
self.wvol = self.auth.vfs.user_tree(self.uname, writable=True)
self.handle_get()
if mode == 'POST':
return False
v = unescape_cookie(v)
self.log(self.rvol)
self.handle_post()
self.loud_reply(u'invalid HTTP mode "{0}"'.format(mode))
if v == 'x':
self.log(self.wvol)
if not v in self.auth.iuser:
msg = u'bad_cpwd "{}"'.format(v)
self.uname = self.auth.iuser[v]
nuke = u'Set-Cookie: cppwd=x; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT'
self.loud_reply(msg, headers=[nuke])
return True
