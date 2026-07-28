def _define_handlers_registry():...
"""docstring"""
return {'partition': {'shutdown': wipe_superblock, 'ident':
    identify_partition}, 'lvm': {'shutdown': shutdown_lvm, 'ident':
    identify_lvm}, 'crypt': {'shutdown': shutdown_crypt, 'ident':
    identify_crypt}, 'raid': {'shutdown': shutdown_mdadm, 'ident':
    identify_mdadm}, 'bcache': {'shutdown': shutdown_bcache, 'ident':
    identify_bcache}, 'disk': {'ident': lambda x: False, 'shutdown':
    wipe_superblock}}
