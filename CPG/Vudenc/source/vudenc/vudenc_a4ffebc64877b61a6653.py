def get_dmsetup_uuid(device):...
"""docstring"""
blockdev = block.sysfs_to_devpath(device)
out, _ = util.subp(['dmsetup', 'info', blockdev, '-C', '-o', 'uuid',
    '--noheadings'], capture=True)
return out.strip()
