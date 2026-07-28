from google.appengine.ext import db
import logging
ROLES = ['user', 'editor', 'superuser']
timestamp = db.DateTimeProperty(auto_now_add=True)
description = db.StringProperty(required=True)
email = db.StringProperty()
user_id = db.StringProperty()
token = db.StringProperty()
user_roles = db.StringListProperty()
requested_roles = db.StringListProperty()
def check_token(token):...
return Authorization.all().filter('token =', token).get()
