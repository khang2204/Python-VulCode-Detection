@inlineCallbacks...
if self.http_server:
yield maybeDeferred(self.http_server.stopListening)
yield super(TestMakeTorrent, self).tearDown()
