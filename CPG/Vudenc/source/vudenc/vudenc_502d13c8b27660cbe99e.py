def identify_partition(device):...
"""docstring"""
path = os.path.join(block.sys_block_path(device), 'partition')
return os.path.exists(path)
