def identify_lvm(device):...
"""docstring"""
return block.path_to_kname(device).startswith('dm') and get_dmsetup_uuid(device
    ).startswith('LVM')
