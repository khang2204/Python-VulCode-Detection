def __init__(self, browser, task_id, base_url=None):...
GenericRequest.__init__(self, browser, base_url)
self.url = '%stasks/%s/description' % (self.base_url, task_id)
self.task_id = task_id
