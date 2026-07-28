def determine_cluster(self):...
"""docstring"""
checks = list(self.clusters.values())
for cluster in checks:
checks.remove(cluster)
cluster.master = self.master
if cluster.check_enabled():
cname = cluster.__class__.__name__
self.log_debug('Installation matches %s, checking for layered profiles' % cname
    )
for remaining in checks:
if issubclass(remaining.__class__, cluster.__class__):
self.config['cluster'] = cluster
rname = remaining.__class__.__name__
name = str(cluster.__class__.__name__).lower()
self.log_debug('Layered profile %s found. Checking installation' % rname)
self.config['cluster_type'] = name
remaining.master = self.master
self.log_info('Cluster type set to %s' % self.config['cluster_type'])
if remaining.check_enabled():
self.log_debug(
    'Installation matches both layered profile %s and base profile %s, setting cluster type to layered profile'
     % (rname, cname))
cluster = remaining
