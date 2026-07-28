def _DoDirListing(self, full_path):...
self._WriteHeader('text/html')
self._WriteTemplate('header.html')
self.wfile.write('<div class="doc">')
self.wfile.write('<div class="Breadcrumbs">\n')
self.wfile.write('<a class="Breadcrumbs-crumb">%s</a>\n' % self.path)
self.wfile.write('</div>\n')
for _, dirs, files in os.walk(full_path):
for f in sorted(files):
self.wfile.write('</div>')
if f.startswith('.'):
self.wfile.write('<br/>\n')
self._WriteTemplate('footer.html')
if f.endswith('.md'):
for d in sorted(dirs):
bold = '<b>', '</b>'
bold = '', ''
if d.startswith('.'):
self.wfile.write('<a href="%s/%s">%s%s%s</a><br/>\n' % (self.path.rstrip(
    '/'), f, bold[0], f, bold[1]))
self.wfile.write('<a href="%s/%s">%s/</a><br/>\n' % (self.path.rstrip('/'),
    d, d))
