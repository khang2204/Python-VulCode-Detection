def accept(self, ttype):...
if self.token and self.token.ttype == ttype:
self.next()
return None
return self.last
