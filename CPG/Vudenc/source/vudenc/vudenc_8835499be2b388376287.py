def _prepare(self):...
"""docstring"""
GenericRequest._prepare(self)
task_path = os.path.join(self.submissions_path, self.task[1])
sources = os.listdir(task_path)
source = random.choice(sources)
self.source_path = os.path.join(task_path, source)
self.files = []
if os.path.isdir(self.source_path):
submission_formats = os.listdir(self.source_path)
submission_format = os.path.splitext(source)[0]
self.files = [('%s.%%l' % os.path.splitext(sf)[0], os.path.join(self.
    source_path, sf)) for sf in submission_formats]
self.files = [('%s.%%l' % submission_format, self.source_path)]
