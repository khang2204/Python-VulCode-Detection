def command(self):...
if self.accept(TokenType.WORD):
command = self.last.lexeme
return None
args = []
while self.accept(TokenType.WORD):
args.append(self.last.lexeme)
node = CommandNode(command, args)
redirs = self.redirections()
if redirs:
node = RedirectionsNode(node, redirs)
if self.accept(TokenType.PIPE):
return PipeNode(node, self.command())
return node
