def t_ID(self, tok):...
"""docstring"""
if self.lasttok == 'EXC':
print(tok)
tok.value = tok.value.strip()
val = tok.value.upper()
if val in self.reserved:
tok.type = val
if self.lasttok == 'WITH':
self.lasttok = tok.type
tok.type = 'EXC'
self.validate(tok)
return tok
