def gen_holders_tree(device):...
"""docstring"""
device = block.sys_block_path(device)
dev_name = block.path_to_kname(device)
holder_paths = [block.sys_block_path(h) for h in get_holders(device)
    ] + block.get_sysfs_partitions(device)
dev_type = next((k for k, v in DEV_TYPES.items() if v['ident'](device)),
    DEFAULT_DEV_TYPE)
return {'device': device, 'dev_type': dev_type, 'name': dev_name, 'holders':
    [gen_holders_tree(h) for h in holder_paths]}
