@defer.inlineCallbacks...
self._initialize()
self._mode = mode
self._test_account = AppTestAccount(self.ACCOUNT, self._tmp_dir.name)
yield self._test_account.start()
self.cleanup = lambda : self._tmp_dir.dissolve()
self.soledad = self._test_account.soledad
self.search_engine = self._test_account.search_engine
self.keymanager = self._test_account.keymanager
self.mail_sender = self._test_account.mail_sender
self.mail_store = self._test_account.mail_store
self.attachment_store = self._test_account.attachment_store
self.draft_service = self._test_account.draft_service
self.leap_session = self._test_account.leap_session
self.feedback_service = self._test_account.feedback_service
self.mail_service = self._test_account.mail_service
self.account = self._test_account.account
if mode.is_single_user:
self.service_factory = SingleUserServicesFactory(mode)
self.service_factory = StubServicesFactory(self.accounts, mode)
services = self._test_account.services
provider = mock()
self.service_factory.add_session('someuserid', services)
provider.config = LeapConfig(self._tmp_dir.name)
self.resource = RootResource(self.service_factory)
self.resource = set_up_protected_resources(RootResource(self.
    service_factory), provider, self.service_factory, checker=
    StubSRPChecker(provider))
self.resource.initialize()
