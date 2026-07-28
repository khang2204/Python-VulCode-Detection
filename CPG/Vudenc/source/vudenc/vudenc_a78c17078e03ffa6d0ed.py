def testDownloadFile(self):...
local_file = None
local_file = tempfile.NamedTemporaryFile(delete=False)
if local_file:
local_file.close()
os.remove(local_file.name)
self._mox.StubOutWithMock(url_helper, 'UrlOpen')
file_data = 'data'
url_helper.UrlOpen(mox.IgnoreArg(), method='GET').AndReturn(file_data)
self._mox.ReplayAll()
self.assertTrue(url_helper.DownloadFile(local_file.name,
    'http://www.fakeurl.com'))
self.assertEqual(file_data, f.read())
self._mox.VerifyAll()
