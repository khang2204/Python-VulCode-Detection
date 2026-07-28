from __future__ import print_function
import os
import threading
from .__init__ import *
"""single level in the virtual fs"""
def __init__(self, realpath, vpath, uread=[], uwrite=[]):...
self.realpath = realpath
self.vpath = vpath
self.uread = uread
self.uwrite = uwrite
self.nodes = {}
def add(self, src, dst):...
"""docstring"""
assert not src.endswith('/')
assert not dst.endswith('/')
if '/' in dst:
name, dst = dst.split('/', 1)
if dst in self.nodes:
if name in self.nodes:
return self.nodes[dst]
vp = '{}/{}'.format(self.vpath, dst).lstrip('/')
return self.nodes[name].add(src, dst)
vn = VFS('{}/{}'.format(self.realpath, name), '{}/{}'.format(self.vpath,
    name).lstrip('/'), self.uread, self.uwrite)
vn = VFS(src, vp)
self.nodes[name] = vn
self.nodes[dst] = vn
return vn.add(src, dst)
return vn
