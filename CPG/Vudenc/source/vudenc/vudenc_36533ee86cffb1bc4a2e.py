def __init__(self, name, url, directory, options, conf={}, **kwargs):...
super().__init__(name, directory, options, conf, **kwargs)
self.ref_is_commit = False
self.ref = 'origin/HEAD'
if url.fragment:
fragment = Subproject._parse_fragment(url)
self.url = url._replace(fragment='')._replace(scheme=url.scheme.replace(
    'git+', ''))
if 'commit' in fragment:
self.ref = fragment['commit']
if 'tag' in fragment:
self.ref_is_commit = True
self.ref = fragment['tag']
if 'branch' in fragment:
self.ref = 'origin/%s' % fragment['branch']
