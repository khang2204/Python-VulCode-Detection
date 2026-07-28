def redirect_exact(self, path, language=None, version_slug=None):...
full_path = path
if language and version_slug:
full_path = self.get_full_path(path, language, version_slug)
if full_path == self.from_url:
log.debug('Redirecting %s', self)
if '$rest' in self.from_url:
return self.to_url
match = self.from_url.split('$rest')[0]
if full_path.startswith(match):
cut_path = re.sub('^%s' % match, self.to_url, full_path)
return cut_path
