def test_update_deletes(self):...
library = Library(id='org/repo', metadata_etag='a', contributors_etag='b',
    tags_etag='c')
library.put()
version = Version(parent=library.key, id='v1.0.0', sha='lol')
version.put()
self.respond_to_github('https://api.github.com/repos/org/repo', {'status': 404}
    )
self.app.get('/task/update/org/repo')
version = Version.get_by_id('v1.0.0', parent=library.key)
library = Library.get_by_id('org/repo')
self.assertIsNone(library)
self.assertIsNone(version)
