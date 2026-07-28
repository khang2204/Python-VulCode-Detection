"""
AJAX/COMET fallback webclient

The AJAX/COMET web client consists of two components running on
twisted and django. They are both a part of the Evennia website url
tree (so the testing website might be located on
http://localhost:4001/, whereas the webclient can be found on
http://localhost:4001/webclient.)

/webclient - this url is handled through django's template
             system and serves the html page for the client
             itself along with its javascript chat program.
/webclientdata - this url is called by the ajax chat using
                 POST requests (long-polling when necessary)
                 The WebClient resource in this module will
                 handle these requests and act as a gateway
                 to sessions connected over the webclient.
"""
import json
import re
import time
from twisted.web import server, resource
from twisted.internet.task import LoopingCall
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.conf import settings
from evennia.utils.ansi import parse_ansi
from evennia.utils import utils
from evennia.utils.text2html import parse_html
from evennia.server import session
_CLIENT_SESSIONS = utils.mod_import(settings.SESSION_ENGINE).SessionStore
_RE_SCREENREADER_REGEX = re.compile('%s' % settings.
    SCREENREADER_REGEX_STRIP, re.DOTALL + re.MULTILINE)
_SERVERNAME = settings.SERVERNAME
_KEEPALIVE = 30
def default(self, obj):...
if isinstance(obj, Promise):
return force_unicode(obj)
return super(LazyEncoder, self).default(obj)
