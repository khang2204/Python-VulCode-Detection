def redirect_sphinx_htmldir(self, path, language=None, version_slug=None):...
if path.endswith('.html'):
log.debug('Redirecting %s', self)
path = path[1:]
to = re.sub('.html$', '/', path)
return self.get_full_path(filename=to, language=language, version_slug=
    version_slug)
