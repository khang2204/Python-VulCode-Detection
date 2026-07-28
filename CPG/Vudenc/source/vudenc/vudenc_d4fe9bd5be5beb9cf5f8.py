def __init__(self, message, deps):...
self.message = message
if isinstance(deps, str) or deps is None:
deps = [deps]
self.deps = [d for d in deps if d is not None]
self.fatal = None in deps
