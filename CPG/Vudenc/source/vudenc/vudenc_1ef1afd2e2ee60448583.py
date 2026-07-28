def parse_cluster_options(self):...
opts = []
if not isinstance(self['cluster_options'], list):
self['cluster_options'] = [self['cluster_options']]
if self['cluster_options']:
for option in self['cluster_options']:
self['cluster_options'] = opts
cluster = option.split('.')[0]
name = option.split('.')[1].split('=')[0]
value = pipes.quote(option.split('=')[1].split()[0])
value = 'True'
opts.append(ClusterOption(name, value, value.__class__, cluster))
