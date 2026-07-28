def __init__(self, browser, username, password, base_url=None):...
GenericRequest.__init__(self, browser, base_url)
self.username = username
self.password = password
self.url = '%slogin' % self.base_url
self.data = {'username': self.username, 'password': self.password, 'next': '/'}
