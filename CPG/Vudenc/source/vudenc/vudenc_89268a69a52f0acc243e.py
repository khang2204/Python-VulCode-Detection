def __init__(self, *args, **kwargs):...
super(HP3PARFCDriver, self).__init__(*args, **kwargs)
self.common = None
self.configuration.append_config_values(hpcommon.hp3par_opts)
self.configuration.append_config_values(san.san_opts)
