def __iter__(self):...
"""docstring"""
while True:
token = self.token()
yield token
if token.ttype == TokenType.EOF:
