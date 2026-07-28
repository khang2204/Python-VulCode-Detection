from google.appengine.api import users as gae_users
from components import auth
from components import config as config_api
from components import decorators
from components import endpoints_webapp2
from components import prpc
import webapp2
from legacy import api as legacy_api
from legacy import swarmbucket_api
import access
import api
import bq
import bulkproc
import config
import expiration
import model
import notifications
import service
import swarming
import user
README_MD = (
    'https://chromium.googlesource.com/infra/infra/+/master/appengine/cr-buildbucket/README.md'
    )
"""Redirects to README.md."""
def get(self):...
return self.redirect(README_MD)
