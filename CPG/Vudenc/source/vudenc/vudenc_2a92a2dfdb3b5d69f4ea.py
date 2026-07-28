def inodeusage(args=None):...
"""docstring"""
cmd = 'df -i'
if args is not None:
cmd = cmd + ' -' + args
ret = {}
out = __salt__['cmd.run'](cmd).splitlines()
for line in out:
if line.startswith('Filesystem'):
return ret
comps = line.split()
if not comps:
if __grains__['kernel'] == 'OpenBSD':
log.warn('Problem parsing inode usage information')
ret[comps[8]] = {'inodes': int(comps[5]) + int(comps[6]), 'used': comps[5],
    'free': comps[6], 'use': comps[7], 'filesystem': comps[0]}
ret[comps[5]] = {'inodes': comps[1], 'used': comps[2], 'free': comps[3],
    'use': comps[4], 'filesystem': comps[0]}
ret = {}
