def _prepare(self):...
GenericRequest._prepare(self)
_, temp_filename = tempfile.mkstemp()
self.files = list(zip(self.submission_format, self.filenames)) + [('input',
    temp_filename)]
