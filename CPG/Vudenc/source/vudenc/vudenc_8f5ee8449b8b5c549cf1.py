import httplib
import types
import collections
import json
import re
import sys
import logging
from StringIO import StringIO
from cgi import parse_header
from urllib import unquote
from twisted.python.failure import Failure
from twisted.internet.defer import inlineCallbacks
from twisted.internet import fdesc
from cyclone.web import RequestHandler, HTTPError, HTTPAuthenticationRequired, StaticFileHandler, RedirectHandler
from cyclone.httpserver import HTTPConnection, HTTPRequest, _BadRequestException
from cyclone import escape, httputil
from cyclone.escape import native_str, parse_qs_bytes
from globaleaks.jobs.statistics_sched import alarm_level
from globaleaks.utils.utility import log, log_remove_escapes, log_encode_html, datetime_now
from globaleaks.utils.mailutils import mail_exception
from globaleaks.settings import GLSetting
from globaleaks.rest import errors
from globaleaks.security import GLSecureTemporaryFile, security_sleep
def validate_host(host_key):...
"""docstring"""
if len(host_key) == 22 and host_key[16:22] == '.onion':
return True
hostchunk = str(host_key).split(':')
if len(hostchunk) == 2:
host_key = hostchunk[0]
if host_key in GLSetting.accepted_hosts:
return True
log.debug('Error in host requested: %s not accepted between: %s ' % (
    host_key, GLSetting.accepted_hosts))
return False
