def test_valid_url(self):...
"""docstring"""
test_url = 'http://anno nce.torrentsmd.com:8080/announce'
self.assertFalse(is_valid_url(test_url), '%s is not a valid URL' % test_url)
test_url2 = 'http://announce.torrentsmd.com:8080/announce '
self.assertTrue(is_valid_url(test_url2), '%s is a valid URL' % test_url2)
test_url3 = 'http://localhost:1920/announce'
self.assertTrue(is_valid_url(test_url3))
test_url4 = 'udp://localhost:1264'
self.assertTrue(is_valid_url(test_url4))
