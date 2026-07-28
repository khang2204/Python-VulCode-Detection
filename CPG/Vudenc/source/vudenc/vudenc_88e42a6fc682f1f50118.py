def act(self):...
self.login()
while True:
task = random.choice(self.tasks)
self.do_step(SubmitRandomRequest(self.browser, task, base_url=self.base_url,
    submissions_path=self.submissions_path))
