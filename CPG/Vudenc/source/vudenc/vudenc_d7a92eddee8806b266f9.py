import json
import logging
import os
import sys
import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2
import common
"""Base class for administrative commands.

  Implement get() and post() methods in the subclasses.
  """
def __init__(self, handler):...
self._handler = handler
@property...
return self._handler.request
