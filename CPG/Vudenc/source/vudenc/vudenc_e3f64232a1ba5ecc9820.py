def __init__(self, base_dir=None):...
"""docstring"""
self.base_dir = base_dir
if not self.base_dir:
self.base_dir = os.path.dirname(os.path.abspath(__file__))
self.test_server = None
self.base_dir = os.path.realpath(os.path.join(self.base_dir, '..'))
self.port = None
self.app_id = None
self.url = None
self.tmp_db = None
self._xsrf_token = None
self._cookie_jar = cookielib.CookieJar()
cookie_processor = urllib2.HTTPCookieProcessor(self._cookie_jar)
redirect_handler = urllib2.HTTPRedirectHandler()
self._opener = urllib2.build_opener(redirect_handler, cookie_processor)
