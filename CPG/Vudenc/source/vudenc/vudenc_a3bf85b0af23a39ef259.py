import logging
import model
import utils
from utils import DateTime, ErrorMessage, Redirect
from utils import db, get_message, html_escape, users
from access import check_user_role
input_size = 10
def text_input(self, name, value):...
"""docstring"""
if isinstance(value, unicode):
if isinstance(value, str):
return u'<input name="%s" value="%s" size=%d>' % (html_escape(name),
    html_escape(value), self.input_size)
value = value.decode('utf-8')
if value is not None:
value = str(value)
value = ''
