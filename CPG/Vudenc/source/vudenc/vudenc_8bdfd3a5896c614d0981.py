@defer.inlineCallbacks...
account = self._accounts[leap_session.user_auth.username]
self._services_by_user[leap_session.user_auth.uuid] = account.services
yield defer.succeed(None)
