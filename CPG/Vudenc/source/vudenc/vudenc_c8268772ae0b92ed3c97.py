@Endpoint('GET', '/lsdir')...
if root_dir is None:
root_dir = '/'
depth = int(depth)
if depth > 5:
logger.warning('[NFS] Limiting depth to maximum value of 5: input depth=%s',
    depth)
root_dir = '{}/'.format(root_dir) if not root_dir.endswith('/') else root_dir
depth = 5
cfs = CephFS()
return {'paths': []}
paths = cfs.get_dir_list(root_dir, depth)
paths = [p[:-1] for p in paths if p != root_dir]
return {'paths': paths}
