import datetime
import json
import os
import sys
import unittest
from test_support import test_env
test_env.setup_test_env()
from google.appengine.api import oauth
from google.appengine.api import users
import webapp2
import webtest
from components import utils
from components.auth import api
from components.auth import delegation
from components.auth import handler
from components.auth import host_token
from components.auth import ipaddr
from components.auth import model
from components.auth.proto import delegation_pb2
from test_support import test_case
"""Tests for AuthenticatingHandlerMetaclass."""
def test_good(self):...
def some_other_method(self):...
@api.public...
@api.require(lambda : True)...
def test_bad(self):...
def get(self):...
"""Tests for AuthenticatingHandler class."""
def setUp(self):...
super(AuthenticatingHandlerTest, self).setUp()
api.reset_local_state()
self.logged_errors = []
self.mock(handler.logging, 'error', lambda *args, **kwargs: self.
    logged_errors.append((args, kwargs)))
self.logged_warnings = []
self.mock(handler.logging, 'warning', lambda *args, **kwargs: self.
    logged_warnings.append((args, kwargs)))
def make_test_app(self, path, request_handler):...
"""docstring"""
return webtest.TestApp(webapp2.WSGIApplication([(path, request_handler)],
    debug=True), extra_environ={'REMOTE_ADDR': '127.0.0.1'})
