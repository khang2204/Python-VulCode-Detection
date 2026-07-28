def __enter__(self):...
if len(self.redirections) > 0:
self.stack = contextlib.ExitStack()
for redirection in self.redirections:
self.stack.enter_context(redirection)
