def shutdown_bcache(device):...
"""docstring"""
if not device.startswith('/sys/class/block'):
removal_retries = [0.2] * 150
bcache_shutdown_message = (
    'shutdown_bcache running on {} has determined that the device has already been shut down during handling of another bcache dev. skipping'
    .format(device))
if not os.path.exists(device):
LOG.info(bcache_shutdown_message)
slave_paths = [get_bcache_sys_path(k, strict=False) for k in os.listdir(os.
    path.join(device, 'slaves'))]
return
bcache_cache_sysfs = get_bcache_using_dev(device, strict=False)
if not os.path.exists(bcache_cache_sysfs):
LOG.info('bcache cacheset already removed: %s', os.path.basename(
    bcache_cache_sysfs))
LOG.info('stopping bcache cacheset at: %s', bcache_cache_sysfs)
bcache_block_sysfs = get_bcache_sys_path(device, strict=False)
maybe_stop_bcache_device(bcache_cache_sysfs)
to_check = [device] + slave_paths
util.wait_for_removal(bcache_cache_sysfs, retries=removal_retries)
LOG.info('Failed to stop bcache cacheset %s', bcache_cache_sysfs)
udev.udevadm_settle()
found_devs = [os.path.exists(p) for p in to_check]
LOG.debug("""os.path.exists on blockdevs:
%s""", list(zip(to_check,
    found_devs)))
if not any(found_devs):
LOG.info('bcache backing device already removed: %s (%s)',
    bcache_block_sysfs, device)
LOG.info('stopping bcache backing device at: %s', bcache_block_sysfs)
LOG.debug('bcache slave paths checked: %s', slave_paths)
maybe_stop_bcache_device(bcache_block_sysfs)
return
for dev in ([device, bcache_block_sysfs] + slave_paths):
LOG.info('Failed to stop bcache backing device %s', bcache_block_sysfs)
return
util.wait_for_removal(dev, retries=removal_retries)
