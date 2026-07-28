def get_from_to_url_display(self):...
if self.redirect_type in ['prefix', 'page', 'exact']:
from_url = self.from_url
return ''
to_url = self.to_url
if self.redirect_type == 'prefix':
to_url = '/{lang}/{version}/'.format(lang=self.project.language, version=
    self.project.default_version)
return '{from_url} -> {to_url}'.format(from_url=from_url, to_url=to_url)
