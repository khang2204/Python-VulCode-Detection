def parse(self):...
"""docstring"""
root = self.commands()
self.expect(TokenType.EOF)
return root
