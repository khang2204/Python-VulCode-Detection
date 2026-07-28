def list_options(self):...
"""docstring"""
print("""
The following cluster options are available:
""")
print('{:15} {:15} {:<10} {:10} {:<}'.format('Cluster', 'Option Name',
    'Type', 'Default', 'Description'))
for cluster in self.clusters:
for opt in self.clusters[cluster].options:
print(
    """
Options take the form of cluster.name=value
E.G. "ovirt.no-database=True" or "pacemaker.offline=False\""""
    )
optln = '{:15} {:15} {:<10} {:<10} {:<10}'.format(opt.cluster, opt.name,
    opt.opt_type.__name__, str(opt.value), opt.description)
print(optln)
