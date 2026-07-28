def testDownloadFileSavingErrors(self):...
file_readonly = None
file_readonly = tempfile.NamedTemporaryFile(delete=False)
if file_readonly:
file_readonly.close()
os.remove(file_readonly.name)
os.chmod(file_readonly.name, stat.S_IREAD)
self._mox.StubOutWithMock(url_helper, 'UrlOpen')
url_helper.UrlOpen(mox.IgnoreArg(), method='GET').AndReturn('data')
self._mox.ReplayAll()
self.assertFalse(url_helper.DownloadFile(file_readonly.name,
    'http://www.fakeurl.com'))
self._mox.VerifyAll()
