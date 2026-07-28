def shutdown_crypt(device):...
"""docstring"""
blockdev = block.sysfs_to_devpath(device)
util.subp(['cryptsetup', 'remove', blockdev], capture=True)
