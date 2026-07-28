def act(self):...
self.login()
while True:
choice = random.random()
task = random.choice(self.tasks)
if choice < 0.1 and self.submissions_path is not None:
self.do_step(SubmitRandomRequest(self.browser, task, base_url=self.base_url,
    submissions_path=self.submissions_path))
if choice < 0.6 and task[2] != []:
self.do_step(TaskStatementRequest(self.browser, task[1], random.choice(task
    [2]), base_url=self.base_url))
self.do_step(TaskRequest(self.browser, task[1], base_url=self.base_url))
