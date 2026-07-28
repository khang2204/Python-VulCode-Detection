def redirect_prefix(self, path, language=None, version_slug=None):...
if path.startswith(self.from_url):
log.debug('Redirecting %s', self)
cut_path = re.sub('^%s' % self.from_url, '', path)
to = self.get_full_path(filename=cut_path, language=language, version_slug=
    version_slug)
return to
