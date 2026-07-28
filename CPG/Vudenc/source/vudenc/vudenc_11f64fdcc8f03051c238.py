def innerFunc():...
i = txt.find(' ')
marker = txt[:i]
describee = ''
content = txt[i + 1:]
self.emph = 1 if marker.find('*') > -1 else 0
self.uncover = 2 if marker.find('+') > -1 else 0
self.kind = 0
self.resume = False
if marker.find('.') > -1:
self.kind = 1
if marker.find(',') > -1:
super(ListItem, self).__init__(slideParser.parse(content, slideLexer), '%s' +
    self.markers[self.kind] % (self.specs[self.emph + self.uncover],
    describee), '\n')
self.kind = 1
if marker.find('=') > -1:
self.resume = True
self.kind = 2
j = content.find('=')
if j == -1:
j = content.find(' ')
if j == -1:
describee = content
describee = content[:j]
content = ' '
content = content[j + 1:]
