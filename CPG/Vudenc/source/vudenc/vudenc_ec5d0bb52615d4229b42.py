def redirection(self):...
if self.accept(TokenType.REDIRECT_OUT):
filename = self.expect(TokenType.WORD).lexeme
if self.accept(TokenType.REDIRECT_APPEND):
return RedirectionHelper(1, (filename, os.O_CREAT | os.O_WRONLY | os.O_TRUNC))
filename = self.expect(TokenType.WORD).lexeme
if self.accept(TokenType.REDIRECT_IN):
return RedirectionHelper(1, (filename, os.O_CREAT | os.O_WRONLY | os.O_APPEND))
filename = self.expect(TokenType.WORD).lexeme
return None
return RedirectionHelper(0, (filename, os.O_RDONLY))
