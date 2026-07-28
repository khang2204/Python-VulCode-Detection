import logging
import os
import sys
import threading
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, os.path.join(ROOT_DIR, 'third_party'))
from depot_tools import auto_stub
from utils import net
def make_fake_response(content, url, headers=None):...
"""docstring"""
headers = dict(headers or {})
headers['Content-Length'] = len(content)
def __init__(self):...
self.content = content
def iter_content(self, chunk_size):...
c = self.content
while c:
yield c[:chunk_size]
def read(self):...
c = c[chunk_size:]
return self.content
