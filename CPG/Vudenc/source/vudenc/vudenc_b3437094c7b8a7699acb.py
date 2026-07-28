import logging
import os
from xml.sax import SAXParseException
from twisted.cred import credentials
from twisted.internet import defer
from twisted.web import util
from twisted.web.error import FlattenerError
from twisted.web.http import UNAUTHORIZED, OK
from twisted.web.resource import IResource, NoResource
from twisted.web.server import NOT_DONE_YET
from twisted.web.static import File
from twisted.web.template import Element, XMLFile, renderElement, renderer
from twisted.python.filepath import FilePath
from pixelated.adapter.welcome_mail import add_welcome_mail
from pixelated.resources import BaseResource, UnAuthorizedResource, IPixelatedSession
log = logging.getLogger(__name__)
def _get_startup_folder():...
path = os.path.dirname(os.path.abspath(__file__))
return os.path.join(path, '..', 'assets')
