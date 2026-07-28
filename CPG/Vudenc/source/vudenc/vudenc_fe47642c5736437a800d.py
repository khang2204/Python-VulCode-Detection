@defer.inlineCallbacks...
yield self._services_factory.create_services_from(leap_session)
if leap_session.fresh_account:
yield add_welcome_mail(leap_session.mail_store)
