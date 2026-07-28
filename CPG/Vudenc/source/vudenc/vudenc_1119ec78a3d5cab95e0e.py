@property...
"""docstring"""
if self._parsed_content_packages:
return self._parsed_content_packages
value = self.config.get(self.section, 'content_packages')
res = []
for this in value.split(','):
this = this.strip()
self._parsed_content_packages = res
name, _sep, path = this.partition(':')
return res
res.append((name, path))
