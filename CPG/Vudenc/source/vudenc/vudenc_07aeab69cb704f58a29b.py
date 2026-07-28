def _parse_options(self):...
"""docstring"""
if self.config['cluster_options']:
for opt in self.config['cluster_options']:
match = False
for option in self.clusters[opt.cluster].options:
if opt.name == option.name:
if not match:
match = True
self._exit('Unknown option provided: %s.%s' % (opt.cluster, opt.name))
option.value = self._validate_option(option, opt)
