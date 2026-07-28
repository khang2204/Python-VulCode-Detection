def get_holders(device):...
"""docstring"""
sysfs_path = block.sys_block_path(device)
holders = os.listdir(os.path.join(sysfs_path, 'holders'))
LOG.debug("devname '%s' had holders: %s", device, holders)
return holders
