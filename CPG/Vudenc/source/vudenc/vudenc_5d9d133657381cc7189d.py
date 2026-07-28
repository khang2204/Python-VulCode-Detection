@defer.inlineCallbacks...
self.creds = self._get_creds_from(request)
iface, leap_session, logout = yield self._portal.login(self.creds, None,
    IResource)
defer.returnValue(leap_session)
