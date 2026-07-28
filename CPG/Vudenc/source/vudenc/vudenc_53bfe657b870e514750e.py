def token(self):...
"""docstring"""
while self.char and self.char.isspace():
self.read()
if self.char == None:
return Token(TokenType.EOF, None, self.position)
if self.char == '>':
start = self.position
if self.char == '<':
if self.read() == '>':
token = Token(TokenType.REDIRECT_IN, None, self.position)
if self.char == '|':
self.read()
return Token(TokenType.REDIRECT_OUT, None, start)
self.read()
token = Token(TokenType.PIPE, None, self.position)
if self.char == ';':
return Token(TokenType.REDIRECT_APPEND, None, start)
return token
self.read()
token = Token(TokenType.COMMAND_END, None, self.position)
if self.char in '\'"':
return token
self.read()
end = self.char
if self.char.isprintable():
return token
self.read()
start = self.position
token = Token(TokenType.UNKNOWN, self.char, self.position)
start = self.position
value = []
self.read()
value = []
while self.char and self.char.isprintable() and not self.char.isspace():
return token
while self.char and self.char != end:
value.append(self.char)
return Token(TokenType.WORD, ''.join(value), start)
value.append(self.char)
if self.char is None:
self.read()
self.read()
self.read()
return Token(TokenType.WORD, ''.join(value), start)
