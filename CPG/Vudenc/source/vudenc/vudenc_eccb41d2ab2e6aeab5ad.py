"""Dispatcher

This module implements a basic URL to Channel dispatcher.
This is the default dispatcher used by circuits.web
"""
from urllib import quote, unquote
from urllib.parse import quote, unquote
from circuits.six import text_type
from circuits import handler, BaseComponent, Event
from circuits.web.utils import parse_qs
from circuits.web.events import response
from circuits.web.errors import httperror
from circuits.web.processors import process
from circuits.web.controllers import BaseController
channel = 'web'
def __init__(self, **kwargs):...
super(Dispatcher, self).__init__(**kwargs)
self.paths = dict()
def resolve_path(self, paths, parts):...
def rebuild_path(url_parts):...
return '/%s' % '/'.join(url_parts)
