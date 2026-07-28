from __future__ import absolute_import
import logging
from twisted.internet import reactor
from twisted.internet.defer import Deferred, inlineCallbacks
from twisted.internet.protocol import Protocol
from twisted.internet.task import deferLater
from twisted.web.client import Agent, HTTPConnectionPool
from twisted.web.http_headers import Headers
import Tribler.Core.Utilities.json_util as json
from Tribler.Core.simpledefs import NTFY_CHANNEL, NTFY_CREDIT_MINING, NTFY_DISCOVERED, NTFY_ERROR, NTFY_FINISHED, NTFY_INSERT, NTFY_MARKET_ON_ASK, NTFY_MARKET_ON_ASK_TIMEOUT, NTFY_MARKET_ON_BID, NTFY_MARKET_ON_BID_TIMEOUT, NTFY_MARKET_ON_PAYMENT_RECEIVED, NTFY_MARKET_ON_PAYMENT_SENT, NTFY_MARKET_ON_TRANSACTION_COMPLETE, NTFY_NEW_VERSION, NTFY_REMOVE, NTFY_STARTED, NTFY_TORRENT, NTFY_TUNNEL, NTFY_UPDATE, NTFY_UPGRADER, NTFY_UPGRADER_TICK, NTFY_WATCH_FOLDER_CORRUPT_TORRENT, SIGNAL_LOW_SPACE, SIGNAL_RESOURCE_CHECK
from Tribler.Core.version import version_id
from Tribler.Test.Core.Modules.RestApi.base_api_test import AbstractApiTest
from Tribler.Test.tools import trial_timeout
from Tribler.pyipv8.ipv8.messaging.anonymization.tunnel import Circuit
"""
    This class is responsible for reading the data received over the event socket.
    """
def __init__(self, messages_to_wait_for, finished, response):...
self.json_buffer = []
self._logger = logging.getLogger(self.__class__.__name__)
self.messages_to_wait_for = messages_to_wait_for + 1
self.finished = finished
self.response = response
def dataReceived(self, data):...
self._logger.info('Received data: %s' % data)
self.json_buffer.append(json.loads(data))
self.messages_to_wait_for -= 1
if self.messages_to_wait_for == 0:
self.response.loseConnection()
def connectionLost(self, reason='done'):...
self.finished.callback(self.json_buffer[1:])
@inlineCallbacks...
yield super(TestEventsEndpoint, self).setUp()
self.events_deferred = Deferred()
self.connection_pool = HTTPConnectionPool(reactor, False)
self.socket_open_deferred = self.tribler_started_deferred.addCallback(self.
    open_events_socket)
self.messages_to_wait_for = 0
@inlineCallbacks...
yield self.close_connections()
yield deferLater(reactor, 0.3, lambda : None)
yield super(TestEventsEndpoint, self).tearDown()
def on_event_socket_opened(self, response):...
response.deliverBody(EventDataProtocol(self.messages_to_wait_for, self.
    events_deferred, response))
def open_events_socket(self, _):...
agent = Agent(reactor, pool=self.connection_pool)
return agent.request('GET', 'http://localhost:%s/events' % self.session.
    config.get_http_api_port(), Headers({'User-Agent': ['Tribler ' +
    version_id]}), None).addCallback(self.on_event_socket_opened)
