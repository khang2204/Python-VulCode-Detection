from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import re
from bs4 import BeautifulSoup
from cmstestsuite.web import GenericRequest, LoginRequest
def test_success(self):...
if not LoginRequest.test_success(self):
return False
fail_re = re.compile('Failed to log in.')
if fail_re.search(self.res_data) is not None:
return False
username_re = re.compile(self.username)
if username_re.search(self.res_data) is None:
return False
return True
