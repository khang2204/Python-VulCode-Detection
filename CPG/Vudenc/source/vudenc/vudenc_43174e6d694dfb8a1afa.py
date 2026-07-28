import json
import multiprocessing
from leap.mail.adaptors.soledad import SoledadMailAdaptor
from leap.srp_session import SRPSession
from mockito import mock
import os
import shutil
import time
import uuid
import random
from leap.mail.imap.account import IMAPAccount
from leap.soledad.client import Soledad
from mock import Mock
from twisted.internet import reactor, defer
from twisted.internet.defer import succeed
from twisted.web.resource import getChildForRequest
from zope.interface import implementer
from twisted.cred import checkers, credentials
from pixelated.adapter.mailstore.leap_attachment_store import LeapAttachmentStore
from pixelated.adapter.services.feedback_service import FeedbackService
from pixelated.application import ServicesFactory, UserAgentMode, SingleUserServicesFactory, set_up_protected_resources
from pixelated.bitmask_libraries.config import LeapConfig
from pixelated.bitmask_libraries.session import LeapSession
from pixelated.config.services import Services
from pixelated.config.site import PixelatedSite
from pixelated.adapter.mailstore import LeapMailStore
from pixelated.adapter.mailstore.searchable_mailstore import SearchableMailStore
from pixelated.adapter.search import SearchEngine
from pixelated.adapter.services.draft_service import DraftService
from pixelated.adapter.services.mail_service import MailService
from pixelated.resources.root_resource import RootResource
from test.support.integration.model import MailBuilder
from test.support.test_helper import request_mock
from test.support.integration.model import ResponseMail
from tempdir import TempDir
INDEX_KEY = (
    'Þ3?\x87ÿÙÓ\x14ð§>\x1f%C{\x16.\\®\x8c\x13§û\x04Ô]+\x8d_íÑ\x8d\x0bI\x8a\x0e¤tm«¿´¥\x99\x00dÕw\x9f\x18¼\x1dÔ_WÒ¶èH\x83\x1bØ\x9d\xad'
    )
def __init__(self, user_id, leap_home):...
self._user_id = user_id
self._leap_home = leap_home
self._uuid = str(uuid.uuid4())
self._mail_address = '%s@pixelated.org' % user_id
self._soledad = None
self._services = None
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
