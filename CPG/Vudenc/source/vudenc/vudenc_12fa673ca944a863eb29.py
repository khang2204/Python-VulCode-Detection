def __init__(self, options, filepath, env_ctx):...
self.filepath = filepath
self.options = options
super(GometaLinter, self).__init__(env_ctx, _go_get)
