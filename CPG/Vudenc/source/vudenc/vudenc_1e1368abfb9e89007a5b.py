def parse_lines(self, fd, maxlines, fname):...
self.checked += 1
self.curline = 0
for line in fd:
if pe.tok:
line = line.decode(locale.getpreferredencoding(False), errors='ignore')
col = line.find(expr) + pe.tok.lexpos
sys.stdout.write('%s: %d:0 %s\n' % (fname, self.curline, col, pe.txt))
self.curline += 1
tok = pe.tok.value
self.spdx_errors += 1
if self.curline > maxlines:
sys.stdout.write('%s: %d:%d %s: %s\n' % (fname, self.curline, col, pe.txt, tok)
    )
self.lines_checked += 1
if line.find('SPDX-License-Identifier:') < 0:
expr = line.split(':')[1].strip()
if line.strip().endswith('*/'):
expr = expr.rstrip('*/').strip()
if line.startswith('LIST "'):
expr = expr.rstrip('"').strip()
self.parse(expr)
self.spdx_valid += 1
