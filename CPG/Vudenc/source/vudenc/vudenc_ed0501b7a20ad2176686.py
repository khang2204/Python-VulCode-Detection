def __init__(self, txt):...
txt = txt.strip()
debug('Txt picked up by col:', txt)
i = txt.find('\n')
head = txt[1:i].strip()
txt = txt[i + 1:]
self.percentage = self.units = 0.0
self.unspecified = 0
if len(head) == 0:
self.unspecified = 1
if head[-1:] == '%':
def innerFunc():...
self.percentage = float(head[:-1]) * 0.01
self.units = float(head)
super(Column, self).__init__(slideParser.parse(txt, slideLexer), after='\n')
Slide.parsingQ.insert(0, innerFunc)
