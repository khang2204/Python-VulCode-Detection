def shutdown_lvm(device):...
"""docstring"""
device = block.sys_block_path(device)
name_file = os.path.join(device, 'dm', 'name')
vg_name, lv_name = lvm.split_lvm_name(util.load_file(name_file))
LOG.debug('running lvremove on %s/%s', vg_name, lv_name)
util.subp(['lvremove', '--force', '--force', '{}/{}'.format(vg_name,
    lv_name)], rcs=[0, 5])
if len(lvm.get_lvols_in_volgroup(vg_name)) == 0:
util.subp(['vgremove', '--force', '--force', vg_name], rcs=[0, 5])
lvm.lvm_scan()
