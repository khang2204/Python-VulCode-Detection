def next(self):...
self.last = self.token
self.token = next(self.tokens, None)
return self.token
