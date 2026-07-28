def get_bcache_using_dev(device, strict=True):...
"""docstring"""
sysfs_path = block.sys_block_path(device)
path = os.path.realpath(os.path.join(sysfs_path, 'bcache', 'cache'))
if strict and not os.path.exists(path):
err = OSError("device '{}' did not have existing syspath '{}'".format(
    device, path))
return path
err.errno = errno.ENOENT
