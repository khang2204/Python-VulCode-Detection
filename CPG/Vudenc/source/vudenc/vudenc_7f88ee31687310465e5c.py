def parse_options(self):...
self.parse_cluster_options()
for opt in ['skip_plugins', 'enable_plugins', 'plugin_options', 'only_plugins'
if self[opt]:
opts = []
if isinstance(self[opt], six.string_types):
self[opt] = [self[opt]]
for option in self[opt]:
opts += option.split(',')
self[opt] = opts
