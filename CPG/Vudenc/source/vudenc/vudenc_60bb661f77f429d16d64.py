from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import logging
import os
import random
import re
import tempfile
from cms.grading.languagemanager import filename_to_language
from cmscommon.crypto import decrypt_number
from cmstestsuite.web import GenericRequest, LoginRequest
logger = logging.getLogger(__name__)
def test_success(self):...
if not LoginRequest.test_success(self):
return False
if self.redirected_to != self.base_url:
return False
return True
