from __future__ import absolute_import
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks, maybeDeferred
from twisted.web.server import Site
from twisted.web.util import Redirect
from Tribler.Core.Utilities.network_utils import get_random_port
from Tribler.Core.Utilities.utilities import http_get, is_valid_url, parse_magnetlink
from Tribler.Test.test_as_server import AbstractServer
from Tribler.Test.tools import trial_timeout
def __init__(self, *argv, **kwargs):...
super(TestMakeTorrent, self).__init__(*argv, **kwargs)
self.http_server = None
def setUpHttpRedirectServer(self, port, redirect_url):...
self.http_server = reactor.listenTCP(port, Site(Redirect(redirect_url)))
@inlineCallbacks...
if self.http_server:
yield maybeDeferred(self.http_server.stopListening)
yield super(TestMakeTorrent, self).tearDown()
def test_parse_magnetlink_lowercase(self):...
"""docstring"""
_, hashed, _ = parse_magnetlink(
    'magnet:?xt=urn:btih:apctqfwnowubxzoidazgaj2ba6fs6juc')
self.assertEqual(hashed, "\x03Å8\x16Íu¨\x1båÈ\x182`'A\x07\x8b/&\x82")
def test_parse_magnetlink_uppercase(self):...
"""docstring"""
_, hashed, _ = parse_magnetlink(
    'magnet:?xt=urn:btih:APCTQFWNOWUBXZOIDAZGAJ2BA6FS6JUC')
self.assertEqual(hashed, "\x03Å8\x16Íu¨\x1båÈ\x182`'A\x07\x8b/&\x82")
def test_valid_url(self):...
"""docstring"""
test_url = 'http://anno nce.torrentsmd.com:8080/announce'
self.assertFalse(is_valid_url(test_url), '%s is not a valid URL' % test_url)
test_url2 = 'http://announce.torrentsmd.com:8080/announce '
self.assertTrue(is_valid_url(test_url2), '%s is a valid URL' % test_url2)
test_url3 = 'http://localhost:1920/announce'
self.assertTrue(is_valid_url(test_url3))
test_url4 = 'udp://localhost:1264'
self.assertTrue(is_valid_url(test_url4))
@trial_timeout(5)...
"""docstring"""
def on_callback(response):...
self.assertEqual(response, magnet_link)
magnet_link = 'magnet:?xt=urn:btih:DC4B96CF85A85CEEDB8ADC4B96CF85A85CEEDB8A'
port = get_random_port()
self.setUpHttpRedirectServer(port, magnet_link)
test_url = 'http://localhost:%d' % port
http_deferred = http_get(test_url).addCallback(on_callback)
return http_deferred
