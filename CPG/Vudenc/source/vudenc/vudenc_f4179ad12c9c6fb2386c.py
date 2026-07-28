def __init__(self, browser, submission_id, base_url=None):...
GenericRequest.__init__(self, browser, base_url)
self.submission_id = submission_id
self.url = '%ssubmission/%s' % (self.base_url, submission_id)
