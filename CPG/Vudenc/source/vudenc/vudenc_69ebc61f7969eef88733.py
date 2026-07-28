def test_update_respects_304(self):...
library = Library(id='org/repo', metadata_etag='a', contributors_etag='b',
    tags_etag='c')
library.put()
self.respond_to_github('https://api.github.com/repos/org/repo', {'status': 304}
    )
self.respond_to_github('https://api.github.com/repos/org/repo/contributors',
    {'status': 304})
self.respond_to_github('https://api.github.com/repos/org/repo/git/refs/tags',
    {'status': 304})
self.app.get('/task/update/org/repo')
tasks = self.tasks.get_filtered_tasks()
self.assertEqual(len(tasks), 0)
