def test_add_element(self):...
response = self.app.get('/manage/add/element/org/repo')
self.assertEqual(response.status_int, 200)
self.assertEqual(response.normal_body, 'OK')
tasks = self.tasks.get_filtered_tasks()
self.assertEqual(len(tasks), 1)
self.assertEqual(tasks[0].url, util.ingest_library_task('org', 'repo',
    'element'))
self.respond_to_github('https://api.github.com/repos/org/repo', 'metadata bits'
    )
self.respond_to_github('https://api.github.com/repos/org/repo/contributors',
    '["a"]')
self.respond_to_github('https://api.github.com/repos/org/repo/git/refs/tags',
    '[{"ref": "refs/tags/v1.0.0", "object": {"sha": "lol"}}]')
response = self.app.get(util.ingest_library_task('org', 'repo', 'element'))
self.assertEqual(response.status_int, 200)
library = Library.get_by_id('org/repo')
self.assertIsNotNone(library)
self.assertIsNone(library.error)
self.assertEqual(library.kind, 'element')
self.assertEqual(library.metadata, 'metadata bits')
self.assertEqual(library.contributors, '["a"]')
self.assertEqual(library.contributor_count, 1)
version = ndb.Key(Library, 'org/repo', Version, 'v1.0.0').get()
self.assertIsNone(version.error)
self.assertEqual(version.sha, 'lol')
tasks = self.tasks.get_filtered_tasks()
self.assertEqual(len(tasks), 2)
self.assertEqual(tasks[1].url, util.ingest_version_task('org', 'repo',
    'v1.0.0') + '?latestVersion=True')
