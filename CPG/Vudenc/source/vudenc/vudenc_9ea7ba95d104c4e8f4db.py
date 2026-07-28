def redirect_page(self, path, language=None, version_slug=None):...
if path == self.from_url:
log.debug('Redirecting %s', self)
to = self.get_full_path(filename=self.to_url.lstrip('/'), language=language,
    version_slug=version_slug)
return to
