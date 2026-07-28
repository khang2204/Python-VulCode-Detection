def test_ingest_version_falls_back(self):...
library = Library(id='org/repo', metadata=
    '{"full_name": "NSS Bob", "stargazers_count": 420, "subscribers_count": 419, "forks": 418, "updated_at": "2011-8-10T13:47:12Z"}'
    , contributor_count=417)
library.tags = json.dumps(['v1.0.0', 'v1.0.1'])
library.put()
version1 = Version(parent=library.key, id='v1.0.0', sha='lol')
version1.put()
version2 = Version(parent=library.key, id='v1.0.1', sha='lol')
version2.put()
self.respond_to('https://raw.githubusercontent.com/org/repo/v1.0.1/README.md',
    chr(248))
tasks = self.tasks.get_filtered_tasks()
self.assertEqual(len(tasks), 0)
self.app.get(util.ingest_version_task('org', 'repo', 'v1.0.1'), params={
    'latestVersion': 'True'})
version2 = version2.key.get()
self.assertEqual(version2.error, 'Could not store README.md as a utf-8 string')
tasks = self.tasks.get_filtered_tasks()
self.assertEqual(len(tasks), 1)
self.assertEqual(tasks[0].url, util.ingest_version_task('org', 'repo',
    'v1.0.0') + '?latestVersion=True')
