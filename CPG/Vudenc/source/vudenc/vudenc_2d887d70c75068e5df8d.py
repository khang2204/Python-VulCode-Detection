@inlineCallbacks...
yield super(TestEventsEndpoint, self).setUp()
self.events_deferred = Deferred()
self.connection_pool = HTTPConnectionPool(reactor, False)
self.socket_open_deferred = self.tribler_started_deferred.addCallback(self.
    open_events_socket)
self.messages_to_wait_for = 0
