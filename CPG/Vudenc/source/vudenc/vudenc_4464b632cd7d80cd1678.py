def assert_clear(base_paths):...
"""docstring"""
valid = 'disk', 'partition'
if not isinstance(base_paths, (list, tuple)):
base_paths = [base_paths]
base_paths = [block.sys_block_path(path) for path in base_paths]
for holders_tree in [gen_holders_tree(p) for p in base_paths]:
if any(holder_type not in valid and path not in base_paths for holder_type,
