@property...
if self._services is None:
services = mock(Services)
return self._services
services.keymanager = self.keymanager
services.mail_service = self.mail_service
services.draft_service = self.draft_service
services.search_engine = self.search_engine
services.feedback_service = self.feedback_service
services._leap_session = self.leap_session
self._services = services
self.leap_session.close = lambda : 'mocked'
