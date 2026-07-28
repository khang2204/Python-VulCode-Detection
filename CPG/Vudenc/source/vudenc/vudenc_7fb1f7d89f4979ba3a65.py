import os
import sys
import zlib
import time
import logging as logger
import urlparse
from datetime import datetime, timedelta
import cPickle as pickle
logger.info('cPickle module not available')
sys.setrecursionlimit(10000)
import pickle
"""
    Dictionary interface that stores cached
    values in the file system rather than in memory.
    The file path is formed from an md5 hash of the key.
    """
def __init__(self, cache_dir='cache', expires=timedelta(days=30), compress=True...
"""docstring"""
self.cache_dir = cache_dir
self.expires = expires
self.compress = compress
def __getitem__(self, url):...
"""docstring"""
path = self.url_to_path(url)
if os.path.exists(path):
data = fp.read()
def __setitem__(self, url, result):...
if self.compress:
"""docstring"""
logger.info('Loading...')
result = pickle.loads(data)
path = self.url_to_path(url)
data = zlib.decompress(data)
return result
folder = os.path.dirname(path)
if not os.path.exists(folder):
os.makedirs(folder)
data = pickle.dumps(result)
if self.compress:
logger.info('Saving...')
fp.write(data)
data = zlib.compress(data)
def __delitem__(self, url):...
"""docstring"""
path = self.url_to_path(url)
os.remove(path)
def url_to_path(self, url):...
os.removedirs(os.path.dirname(path))
"""docstring"""
components = urlparse.urlsplit(url)
path = components.path
if not path:
path = '/index.html'
if path.endswith('/'):
filename = components.netloc + path + components.query
path += 'index.html'
filename = '/'.join(segment[:255] for segment in filename.split('/'))
return os.path.join(self.cache_dir, filename)
