from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import codecs
import datetime
import io
import os
import sys
import time
import traceback
import urllib
import requests
debug = False
def __init__(self):...
self.xsrf_token = None
self.session = requests.Session()
def read_xsrf_token(self, url):...
response = self.session.get(url)
for cookie in response.cookies:
if cookie.name == '_xsrf':
def login(self, login_request):...
self.xsrf_token = cookie.value
self.read_xsrf_token(login_request.base_url)
login_request.execute()
def do_request(self, url, data=None, file_names=None):...
"""docstring"""
if file_names is None:
if data is None:
data = data.copy()
for fobj in file_objs.itervalues():
return response
response = self.session.get(url)
data = data.copy()
data['_xsrf'] = self.xsrf_token
fobj.close()
data['_xsrf'] = self.xsrf_token
file_objs = dict((k, io.open(v, 'rb')) for k, v in file_names)
response = self.session.post(url, data)
response = self.session.post(url, data, files=file_objs)
