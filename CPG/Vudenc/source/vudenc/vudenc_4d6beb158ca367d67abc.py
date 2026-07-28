def __init__(self, *args, **kwargs):...
execute = kwargs.pop('execute', self.san_execute)
super(SanDriver, self).__init__(*args, execute=execute, **kwargs)
self.configuration.append_config_values(san_opts)
self.run_local = self.configuration.san_is_local
self.sshpool = None
