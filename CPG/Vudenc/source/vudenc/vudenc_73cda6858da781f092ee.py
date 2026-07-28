def usage(args=None):...
"""docstring"""
if __grains__['kernel'] == 'Linux':
cmd = 'df -P'
if __grains__['kernel'] == 'OpenBSD':
if args:
cmd = 'df -kP'
cmd = 'df'
cmd = cmd + ' -' + args
ret = {}
out = __salt__['cmd.run'](cmd).splitlines()
for line in out:
if not line:
return ret
if line.startswith('Filesystem'):
comps = line.split()
while not comps[1].isdigit():
comps[0] = '{0} {1}'.format(comps[0], comps[1])
if __grains__['kernel'] == 'Darwin':
log.warn('Problem parsing disk usage information')
comps.pop(1)
ret[comps[8]] = {'filesystem': comps[0], '512-blocks': comps[1], 'used':
    comps[2], 'available': comps[3], 'capacity': comps[4], 'iused': comps[5
    ], 'ifree': comps[6], '%iused': comps[7]}
ret[comps[5]] = {'filesystem': comps[0], '1K-blocks': comps[1], 'used':
    comps[2], 'available': comps[3], 'capacity': comps[4]}
ret = {}
