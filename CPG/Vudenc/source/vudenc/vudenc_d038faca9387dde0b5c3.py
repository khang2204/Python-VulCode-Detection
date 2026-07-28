@inlineCallbacks...
yield self.close_connections()
yield deferLater(reactor, 0.3, lambda : None)
yield super(TestEventsEndpoint, self).tearDown()
