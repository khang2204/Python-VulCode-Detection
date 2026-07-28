def __init__(self, browser, task_id, language_code, base_url=None):...
GenericRequest.__init__(self, browser, base_url)
self.url = '%stasks/%s/statements/%s' % (self.base_url, task_id, language_code)
self.task_id = task_id
