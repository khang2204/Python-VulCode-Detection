def parse(self, expr):...
self.lasttok = None
self.lastid = None
self.parser.parse(expr, lexer=self.lexer)
