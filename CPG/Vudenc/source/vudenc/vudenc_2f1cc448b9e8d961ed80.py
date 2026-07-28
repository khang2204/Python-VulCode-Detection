def __init__(self, name, url, directory, options, conf={}, **kwargs):...
super().__init__(name, directory, options, conf={}, **kwargs)
self.rev = 'HEAD'
fragment = url.fragment and Subproject._parse_fragment(url) or {}
rev = fragment.get('rev', None)
branch = fragment.get('branch', None)
tag = fragment.get('tag', None)
if (branch or tag) and self.url.path.endswith('trunk'):
url = url._replace(path=self.url.path[:-5])
if branch:
url = url._replace(path=join(url.path, 'branches', branch))
if tag:
if rev:
url = url._replace(path=join(url.path, 'tags', tag))
url = url._replace(path=url.path + '@' + rev)
self.url = url._replace(fragment='')
self.rev = rev
