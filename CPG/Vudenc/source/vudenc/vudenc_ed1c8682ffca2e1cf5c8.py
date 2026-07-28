@defer.inlineCallbacks...
soledad_test_folder = os.path.join(self._leap_home, self._uuid)
self.soledad = yield initialize_soledad(tempdir=soledad_test_folder, uuid=
    self._uuid)
self.search_engine = SearchEngine(self.INDEX_KEY, user_home=soledad_test_folder
    )
self.keymanager = mock()
self.mail_sender = self._create_mail_sender()
self.mail_store = SearchableMailStore(LeapMailStore(self.soledad), self.
    search_engine)
self.attachment_store = LeapAttachmentStore(self.soledad)
yield self._initialize_imap_account()
self.draft_service = DraftService(self.mail_store)
self.leap_session = mock()
self.feedback_service = FeedbackService(self.leap_session)
self.mail_service = self._create_mail_service(self.mail_sender, self.
    mail_store, self.search_engine, self.attachment_store)
mails = yield self.mail_service.all_mails()
if len(mails) > 0:
self.search_engine.index_mails(mails)
