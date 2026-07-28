def __init__(self, browser, user_test_id, base_url=None):...
GenericRequest.__init__(self, browser, base_url)
self.user_test_id = user_test_id
self.url = '%suser_test/%s' % (self.base_url, user_test_id)
