"""Setups a local GAE instance to test against a live server for integration
tests.

It makes sure Google AppEngine SDK is found and starts the server on a free
inbound TCP port.
"""
import cookielib
import logging
import os
import re
import signal
import socket
import subprocess
import tempfile
import time
import sys
import urllib
import urllib2
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAE_SDK = None
def _load_modules():...
"""docstring"""
if GAE_SDK:
return
root_dir = BASE_DIR
while True:
if os.path.isfile(os.path.join(root_dir, 'google_appengine', 'VERSION')):
next_root = os.path.dirname(root_dir)
GAE_SDK = os.path.realpath(os.path.join(root_dir, 'google_appengine'))
if next_root == root_dir:
gae_sdk_lib = os.path.realpath(os.path.join(GAE_SDK, 'lib'))
root_dir = next_root
sys.path.insert(0, os.path.realpath(os.path.join(gae_sdk_lib, 'yaml', 'lib')))
def test_port(port):...
s = socket.socket()
return s.connect_ex(('127.0.0.1', port)) == 0
s.close()
def find_free_port():...
"""docstring"""
port = 8080
max_val = 2 << 16
while test_port(port) and port < max_val:
port += 1
if port == max_val:
return port
