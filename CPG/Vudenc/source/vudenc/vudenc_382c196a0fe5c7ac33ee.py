def __init__(self, txt):...
headBegin = txt.find('[')
headEnd = txt.find('\n', headBegin)
headSplit = txt.find(' ', headBegin) + 1 or headEnd
opts = txt[headBegin + 1:headSplit].strip()
if len(opts) > 0:
if opts[0] == '.':
super(Slide, self).__init__(slideParser.parse(txt[headEnd:-1], slideLexer),
    self.before % (opts, txt[headSplit:headEnd]), self.after)
if opts == '...':
warn('Slide title: Invalid slide option:', opts)
while len(self.parsingQ) > 0:
opts = '[allowframebreaks]'
float(opts[1:])
warn('Slide title: Invalid shrink specifier:', opts[1:])
opts = ''
self.parsingQ.pop()()
opts = '[shrink=%s]' % opts[1:]
opts = ''
