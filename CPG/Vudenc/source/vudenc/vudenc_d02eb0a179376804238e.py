def commands(self):...
base = self.command()
if self.accept(TokenType.COMMAND_END):
other = self.commands()
return base
if base and other:
return DoubleNode(base, other)
return other
