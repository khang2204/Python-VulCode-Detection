def __init__(self, browser, task, submission_format, filenames, language=...
GenericRequest.__init__(self, browser, base_url)
self.url = '%stasks/%s/test' % (self.base_url, task[1])
self.task = task
self.submission_format = submission_format
self.filenames = filenames
self.data = {}
if language is None:
for filename in filenames:
if language is not None:
lang = filename_to_language(filename)
self.data = {'language': language}
if lang is not None:
language = lang.name
