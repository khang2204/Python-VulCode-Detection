def requestAvatarId(self, credentials):...
leap_auth = SRPSession(credentials.username, uuid.uuid4(), uuid.uuid4(),
    uuid.uuid4())
return defer.succeed(LeapSession(self._leap_provider, leap_auth, None, None,
    None, None))
