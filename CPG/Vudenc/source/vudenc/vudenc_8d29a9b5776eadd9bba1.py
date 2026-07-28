def __init__(self, browser, task, base_url=None, submissions_path=None):...
GenericRequest.__init__(self, browser, base_url)
self.url = '%stasks/%s/submit' % (self.base_url, task[1])
self.task = task
self.submissions_path = submissions_path
self.data = {}
