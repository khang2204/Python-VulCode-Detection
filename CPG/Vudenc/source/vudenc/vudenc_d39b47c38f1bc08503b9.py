"""The superclass of all handlers."""
from builtins import object
from future import standard_library
standard_library.install_aliases()
import base64
import cgi
import datetime
import json
import logging
import os
import re
import sys
import traceback
import urllib.parse
import jinja2
import webapp2
from base import utils
from config import db_config
from config import local_config
from datastore import ndb
from google_cloud_utils import storage
from libs import auth
from libs import form
from libs import helpers
from system import environment
def add_jinja2_filter(name, fn):...
_JINJA_ENVIRONMENT.filters[name] = fn
"""Json encoder."""
_EPOCH = datetime.datetime.utcfromtimestamp(0)
def default(self, obj):...
if isinstance(obj, ndb.Model):
dict_obj = obj.to_dict()
if isinstance(obj, datetime.datetime):
dict_obj['id'] = obj.key.id()
return int((obj - self._EPOCH).total_seconds())
if hasattr(obj, 'to_dict'):
return dict_obj
return obj.to_dict()
if isinstance(obj, cgi.FieldStorage):
return str(obj)
def format_time(dt):...
"""docstring"""
return '{t.day} {t:%b} {t:%y} {t:%X} PDT'.format(t=dt)
