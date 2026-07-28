def _DoRawSourceFile(self, full_path):...
self._WriteHeader('text/html')
self._WriteTemplate('header.html')
self.wfile.write('<table class="FileContents">')
data = fp.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'
    ).replace('"', '&quot;')
for i, line in enumerate(data.splitlines(), start=1):
self.wfile.write(
    '<tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum"><a name="%(num)s" onclick="window.location.hash=%(quot)s#%(num)s%(quot)s">%(num)s</a></td><td class="FileContents-lineContents">%(line)s</td></tr>'
     % {'num': i, 'quot': "'", 'line': line})
self.wfile.write('</table>')
self._WriteTemplate('footer.html')
