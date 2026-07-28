def get_bcache_sys_path(device, strict=True):...
"""docstring"""
sysfs_path = block.sys_block_path(device, strict=strict)
path = os.path.join(sysfs_path, 'bcache')
if strict and not os.path.exists(path):
err = OSError("device '{}' did not have existing syspath '{}'".format(
    device, path))
return path
err.errno = errno.ENOENT
