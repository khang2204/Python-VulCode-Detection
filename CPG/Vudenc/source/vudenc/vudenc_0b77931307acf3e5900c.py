def redirect_sphinx_html(self, path, language=None, version_slug=None):...
for ending in ['/', '/index.html']:
if path.endswith(ending):
log.debug('Redirecting %s', self)
path = path[1:]
to = re.sub(ending + '$', '.html', path)
return self.get_full_path(filename=to, language=language, version_slug=
    version_slug)
