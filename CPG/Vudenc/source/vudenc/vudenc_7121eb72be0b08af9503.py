def shutdown_mdadm(device):...
"""docstring"""
blockdev = block.sysfs_to_devpath(device)
LOG.debug('using mdadm.mdadm_stop on dev: %s', blockdev)
mdadm.mdadm_stop(blockdev)
for wait in MDADM_RELEASE_RETRIES:
LOG.critical('Failed to stop mdadm device %s', device)
if mdadm.md_present(block.path_to_kname(blockdev)):
if mdadm.md_present(block.path_to_kname(blockdev)):
if os.path.exists('/proc/mdstat'):
time.sleep(wait)
LOG.debug('%s has been removed', blockdev)
LOG.critical('/proc/mdstat:\n%s', util.load_file('/proc/mdstat'))
