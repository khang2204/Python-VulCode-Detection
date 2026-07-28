def execute(self, raw):...
"""docstring"""
tokens = Tokenizer(raw)
parser = Parser(tokens)
root = parser.parse()
if root:
root.execute(self.builtins)
root.wait()
