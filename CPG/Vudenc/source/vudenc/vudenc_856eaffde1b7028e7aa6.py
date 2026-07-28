"""Internal bot API handlers."""
import base64
import json
import logging
import textwrap
import webob
import webapp2
from google.appengine.api import app_identity
from google.appengine.api import datastore_errors
from google.appengine.datastore import datastore_query
from google.appengine import runtime
from google.appengine.ext import ndb
from components import auth
from components import ereporter2
from components import utils
from server import acl
from server import bot_code
from server import bot_management
from server import stats
from server import task_pack
from server import task_request
from server import task_result
from server import task_scheduler
from server import task_to_run
def has_unexpected_subset_keys(expected_keys, minimum_keys, actual_keys, name):...
"""docstring"""
actual_keys = frozenset(actual_keys)
superfluous = actual_keys - expected_keys
missing = minimum_keys - actual_keys
if superfluous or missing:
msg_missing = ' missing: %s' % sorted(missing) if missing else ''
def has_unexpected_keys(expected_keys, actual_keys, name):...
msg_superfluous = ' superfluous: %s' % sorted(superfluous
    ) if superfluous else ''
"""docstring"""
return 'Unexpected %s%s%s; did you make a typo?' % (name, msg_missing,
    msg_superfluous)
return has_unexpected_subset_keys(expected_keys, expected_keys, actual_keys,
    name)
