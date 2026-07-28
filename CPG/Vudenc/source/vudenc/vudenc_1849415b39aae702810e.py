def __init__(self, txt):...
txt = txt.strip()[:-1]
i = txt.find('\n')
head = txt[:i].strip()
txt = txt[i + 1:]
kind = ''
if head[1] == '!':
kind = 'alert'
head = head[2:]
def innerFunc():...
super(Box, self).__init__(slideParser.parse(txt, slideLexer), self.begin %
    (kind, head), self.end % kind)
Slide.parsingQ.insert(0, innerFunc)
