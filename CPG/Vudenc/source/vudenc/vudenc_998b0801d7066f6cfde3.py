def __init__(self, browser, base_url=None):...
if base_url is None:
base_url = 'http://localhost:8888/'
self.browser = browser
self.base_url = base_url
self.outcome = None
self.start_time = None
self.stop_time = None
self.duration = None
self.exception_data = None
self.url = None
self.data = None
self.files = None
self.status_code = None
self.response = None
self.res_data = None
self.redirected_to = None
