def __init__(self, browser, task, submission_num, base_url=None):...
GenericRequest.__init__(self, browser, base_url)
self.url = '%stasks/%s/submissions/%s/token' % (self.base_url, task[1],
    submission_num)
self.task = task
self.submission_num = submission_num
self.data = {}
