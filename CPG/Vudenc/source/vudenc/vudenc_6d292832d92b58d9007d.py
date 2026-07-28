def __init__(self, tokens):...
self.tokens = iter(tokens)
self.token = None
self.last = None
self.next()
