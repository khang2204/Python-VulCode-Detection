@memoized_property...
"""docstring"""
rebases = {self.dist.real_home: '/dev/null/remapped_by_pants/java_home/',
    get_buildroot(): '/dev/null/remapped_by_pants/buildroot/', self.
    _zinc_factory.get_options().pants_workdir:
    '/dev/null/remapped_by_pants/workdir/'}
return '-rebase-map', ','.join('{}:{}'.format(src, dst) for src, dst in
    rebases.items())
