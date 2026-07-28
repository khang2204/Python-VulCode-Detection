@defer.inlineCallbacks...
user_id = leap_session.user_auth.uuid
if not self._services_factory.is_logged_in(user_id):
yield self._services_factory.create_services_from(leap_session)
self._init_http_session(request, user_id)
