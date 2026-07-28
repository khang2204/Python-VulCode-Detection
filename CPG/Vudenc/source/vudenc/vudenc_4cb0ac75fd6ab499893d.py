def test_ingest_commit(self):...
self.respond_to_github('https://api.github.com/repos/org/repo', 'metadata bits'
    )
self.respond_to_github('https://api.github.com/repos/org/repo/contributors',
    '["a"]')
self.app.get(util.ingest_commit_task('org', 'repo'), params={'commit':
    'commit-sha', 'url': 'url'})
library = Library.get_by_id('org/repo')
self.assertIsNotNone(library)
self.assertIsNone(library.error)
self.assertFalse(library.ingest_versions)
version = Version.get_by_id(parent=library.key, id='commit-sha')
self.assertEqual(version.sha, 'commit-sha')
self.assertEqual(version.url, 'url')
tasks = self.tasks.get_filtered_tasks()
self.assertEqual(len(tasks), 1)
self.assertEqual(tasks[0].url, util.ingest_version_task('org', 'repo',
    'commit-sha'))
