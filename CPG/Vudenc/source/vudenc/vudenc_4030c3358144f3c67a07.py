def flatten_holders_tree(tree, level=0):...
"""docstring"""
device = tree['device']
if device in reg:
level = max(reg[device]['level'], level)
reg[device] = {'level': level, 'device': device, 'dev_type': tree['dev_type']}
for holder in tree['holders']:
flatten_holders_tree(holder, level=level + 1)
