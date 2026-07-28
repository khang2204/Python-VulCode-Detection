def test_ingest_version(self):...
library = Library(id='org/repo', metadata=
    '{"full_name": "NSS Bob", "stargazers_count": 420, "subscribers_count": 419, "forks": 418, "updated_at": "2011-8-10T13:47:12Z"}'
    , contributor_count=417)
version = Version(parent=library.key, id='v1.0.0', sha='lol')
library.put()
version.put()
self.respond_to('https://raw.githubusercontent.com/org/repo/v1.0.0/README.md',
    'README')
self.respond_to('https://raw.githubusercontent.com/org/repo/v1.0.0/bower.json',
    '{}')
self.respond_to_github('https://api.github.com/markdown', '<html>README</html>'
    )
response = self.app.get(util.ingest_version_task('org', 'repo', 'v1.0.0'))
self.assertEqual(response.status_int, 200)
version = version.key.get()
self.assertIsNone(version.error)
readme = ndb.Key(Library, 'org/repo', Version, 'v1.0.0', Content, 'readme'
    ).get()
self.assertEqual(readme.content, 'README')
readme_html = ndb.Key(Library, 'org/repo', Version, 'v1.0.0', Content,
    'readme.html').get()
self.assertEqual(readme_html.content, '<html>README</html>')
bower = ndb.Key(Library, 'org/repo', Version, 'v1.0.0', Content, 'bower').get()
self.assertEqual(bower.content, '{}')
