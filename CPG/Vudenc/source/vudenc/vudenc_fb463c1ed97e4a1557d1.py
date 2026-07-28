"""Auth management UI handlers."""
import functools
import json
import os
import re
import webapp2
from components import template
from components import utils
from . import acl
from . import rest_api
from .. import api
from .. import change_log
from .. import handler
from .. import model
from .. import replication
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    'templates')
_ui_app_name = 'Unknown'
_ui_data_callback = None
_ui_navbar_tabs = ()
def configure_ui(app_name, ui_tabs=None, ui_data_callback=None):...
"""docstring"""
_ui_app_name = app_name
_ui_data_callback = ui_data_callback
if ui_tabs is not None:
assert all(issubclass(cls, UINavbarTabHandler) for cls in ui_tabs)
template.bootstrap({'auth': TEMPLATES_DIR})
_ui_navbar_tabs = tuple(ui_tabs)
def get_ui_routes():...
"""docstring"""
routes = []
for cls in _ui_navbar_tabs:
routes.extend(cls.get_webapp2_routes())
routes.extend([webapp2.Route('/auth', MainHandler), webapp2.Route(
    '/auth/bootstrap', BootstrapHandler, name='bootstrap'), webapp2.Route(
    '/auth/bootstrap/oauth', BootstrapOAuthHandler), webapp2.Route(
    '/auth/link', LinkToPrimaryHandler)])
return routes
