"""Unittest to exercise the code in url_helper.py."""
import logging
import os
import stat
import StringIO
import sys
import tempfile
import time
import unittest
import urllib
import urllib2
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)
import test_env
test_env.setup_test_env()
from depot_tools import auto_stub
from third_party.mox import mox
import url_helper
def setUp(self):...
self._mox = mox.Mox()
self.mock(logging, 'error', lambda *_: None)
self.mock(logging, 'exception', lambda *_: None)
self.mock(logging, 'info', lambda *_: None)
self.mock(logging, 'warning', lambda *_: None)
self._mox.StubOutWithMock(time, 'sleep')
self._mox.StubOutWithMock(urllib2, 'urlopen')
def tearDown(self):...
self._mox.UnsetStubs()
def testUrlOpenInvalidTryCount(self):...
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen('url', max_tries=-1), None)
self._mox.VerifyAll()
def testUrlOpenInvalidWaitDuration(self):...
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen('url', wait_duration=-1), None)
self._mox.VerifyAll()
def testUrlOpenGETSuccess(self):...
url = 'http://my.url.com'
response = 'True'
url_helper.urllib2.urlopen(mox.StrContains(url), timeout=mox.IgnoreArg()
    ).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen(url, method='GET'), response)
self._mox.VerifyAll()
def testUrlOpenPOSTSuccess(self):...
url = 'http://my.url.com'
response = 'True'
url_helper.urllib2.urlopen(url, mox.IgnoreArg(), timeout=mox.IgnoreArg()
    ).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen(url, method='POST'), response)
self._mox.VerifyAll()
def testUrlOpenPOSTFORMSuccess(self):...
url = 'http://my.url.com'
response = 'True'
url_helper.urllib2.urlopen(mox.IsA(urllib2.Request), timeout=mox.IgnoreArg()
    ).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen(url, method='POSTFORM'), response)
self._mox.VerifyAll()
def testUrlOpenSuccessAfterFailure(self):...
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndRaise(urllib2.URLError('url'))
time.sleep(mox.IgnoreArg())
response = 'True'
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen('url', max_tries=2), response)
self._mox.VerifyAll()
def testUrlOpenFailure(self):...
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndRaise(urllib2.URLError('url'))
self._mox.ReplayAll()
self.assertIsNone(url_helper.UrlOpen('url', max_tries=1))
self._mox.VerifyAll()
def testUrlOpenHTTPErrorNoRetry(self):...
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndRaise(urllib2.HTTPError('url', 400, 'error message',
    None, None))
self._mox.ReplayAll()
self.assertIsNone(url_helper.UrlOpen('url', max_tries=10))
self._mox.VerifyAll()
def testUrlOpenHTTPErrorWithRetry(self):...
response = 'response'
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndRaise(urllib2.HTTPError('url', 500, 'error message',
    None, None))
time.sleep(mox.IgnoreArg())
url_helper.urllib2.urlopen(mox.IgnoreArg(), mox.IgnoreArg(), timeout=mox.
    IgnoreArg()).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(response, url_helper.UrlOpen('url', max_tries=10))
self._mox.VerifyAll()
def testEnsureCountKeyIncludedInOpen(self):...
attempts = 5
for i in range(attempts):
encoded_data = urllib.urlencode({url_helper.swarm_constants.COUNT_KEY: i})
self._mox.ReplayAll()
url_helper.urllib2.urlopen(mox.IgnoreArg(), encoded_data, timeout=mox.
    IgnoreArg()).AndRaise(urllib2.URLError('url'))
self.assertEqual(url_helper.UrlOpen('url', max_tries=attempts), None)
if i != attempts - 1:
self._mox.VerifyAll()
time.sleep(mox.IgnoreArg())
def testCountKeyInData(self):...
data = {url_helper.swarm_constants.COUNT_KEY: 1}
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen('url', data=data), None)
self._mox.VerifyAll()
def testNonAcsiiData(self):...
data = {'r': u'not ascii £ һ'}
url = 'http://my.url.com'
response = 'True'
url_helper.urllib2.urlopen(mox.StrContains(url), mox.IgnoreArg(), timeout=
    mox.IgnoreArg()).AndReturn(StringIO.StringIO(response))
self._mox.ReplayAll()
self.assertEqual(url_helper.UrlOpen(url, data=data), response)
self._mox.VerifyAll()
def testDownloadFile(self):...
local_file = None
local_file = tempfile.NamedTemporaryFile(delete=False)
if local_file:
def testDownloadFileDownloadError(self):...
local_file.close()
os.remove(local_file.name)
fake_file = 'fake_local_file.fake'
if os.path.exists(fake_file):
def testDownloadFileSavingErrors(self):...
self._mox.StubOutWithMock(url_helper, 'UrlOpen')
self._mox.StubOutWithMock(url_helper, 'UrlOpen')
os.remove(fake_file)
file_readonly = None
file_data = 'data'
url_helper.UrlOpen(mox.IgnoreArg(), method='GET').AndReturn(None)
file_readonly = tempfile.NamedTemporaryFile(delete=False)
if file_readonly:
def testEncodeMultipartFormData(self):...
url_helper.UrlOpen(mox.IgnoreArg(), method='GET').AndReturn(file_data)
self._mox.ReplayAll()
file_readonly.close()
os.remove(file_readonly.name)
fields = [('x', 'y'), (1, 2)]
self._mox.ReplayAll()
self.assertFalse(url_helper.DownloadFile(fake_file, 'http://www.fakeurl.com'))
os.chmod(file_readonly.name, stat.S_IREAD)
files = [('key', 'filename', 'file data')]
self.assertTrue(url_helper.DownloadFile(local_file.name,
    'http://www.fakeurl.com'))
self._mox.VerifyAll()
self._mox.StubOutWithMock(url_helper, 'UrlOpen')
content_type, body = url_helper.EncodeMultipartFormData()
self.assertEqual(file_data, f.read())
url_helper.UrlOpen(mox.IgnoreArg(), method='GET').AndReturn('data')
self.assertTrue(content_type.startswith('multipart/form-data; boundary='))
self._mox.VerifyAll()
self._mox.ReplayAll()
self.assertEqual('', body)
self.assertFalse(url_helper.DownloadFile(file_readonly.name,
    'http://www.fakeurl.com'))
content_type, body = url_helper.EncodeMultipartFormData(fields=fields)
self._mox.VerifyAll()
self.assertTrue(content_type.startswith('multipart/form-data; boundary='))
self.assertTrue('name="x"\r\n\r\ny' in body, body)
self.assertTrue('name="1"\r\n\r\n2' in body, body)
content_type, body = url_helper.EncodeMultipartFormData(files=files)
self.assertTrue(content_type.startswith('multipart/form-data; boundary='))
self.assertTrue('name="key"; filename="filename"' in body, body)
self.assertTrue('file data' in body, body)
content_type, body = url_helper.EncodeMultipartFormData(fields=fields,
    files=files)
self.assertTrue(content_type.startswith('multipart/form-data; boundary='))
self.assertTrue('name="x"\r\n\r\ny' in body, body)
self.assertTrue('name="1"\r\n\r\n2' in body, body)
if __name__ == '__main__':
logging.disable(logging.FATAL)
unittest.main()
