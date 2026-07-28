def __call__(self, msg, arguments, errorSink=None):...
if not arguments.strip():
return
p1, _, p2 = self._parse_instruction(arguments)
self.reply(msg,
    'could not parse your request: {}. please use format: poly1 mod poly2 in GF(p)[x]'
    .format(err))
d, r = divmod(p1, p2)
self.reply(msg, 'division by zero')
self.reply(msg, '{a} // {b} = {d}; remainder: {r}'.format(a=p1, b=p2, d=d, r=r)
    )
return
return
