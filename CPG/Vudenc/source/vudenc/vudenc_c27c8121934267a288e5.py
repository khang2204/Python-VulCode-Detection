def versions(self):...
conn = sqlite3.connect(':memory:')
self.prepare_connection(conn)
sqlite_version = conn.execute('select sqlite_version()').fetchone()[0]
sqlite_extensions = {}
for extension, testsql, hasversion in (('json1', "SELECT json('{}')", False
fts_versions = []
result = conn.execute(testsql)
for fts in ('FTS5', 'FTS4', 'FTS3'):
if hasversion:
datasette_version = {'version': __version__}
conn.execute('CREATE VIRTUAL TABLE v{fts} USING {fts} (data)'.format(fts=fts))
sqlite_extensions[extension] = result.fetchone()[0]
sqlite_extensions[extension] = None
if self.version_note:
fts_versions.append(fts)
datasette_version['note'] = self.version_note
return {'python': {'version': '.'.join(map(str, sys.version_info[:3])),
    'full': sys.version}, 'datasette': datasette_version, 'sqlite': {
    'version': sqlite_version, 'fts_versions': fts_versions, 'extensions':
    sqlite_extensions, 'compile_options': [r[0] for r in conn.execute(
    'pragma compile_options;').fetchall()]}}
