def __init__(self, browser, username, loggedin, base_url=None):...
GenericRequest.__init__(self, browser, base_url)
self.url = self.base_url
self.username = username
self.loggedin = loggedin
