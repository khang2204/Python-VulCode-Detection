def __init__(self, username, password, metrics, tasks, log=None, base_url=...
threading.Thread.__init__(self)
self.username = username
self.password = password
self.metrics = metrics
self.tasks = tasks
self.log = log
self.base_url = base_url
self.submissions_path = submissions_path
self.name = 'Actor thread for user %s' % self.username
self.browser = Browser()
self.die = False
