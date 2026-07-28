def plan_shutdown_holder_trees(holders_trees):...
"""docstring"""
reg = {}
if not isinstance(holders_trees, (list, tuple)):
holders_trees = [holders_trees]
def flatten_holders_tree(tree, level=0):...
"""docstring"""
device = tree['device']
if device in reg:
level = max(reg[device]['level'], level)
reg[device] = {'level': level, 'device': device, 'dev_type': tree['dev_type']}
for holder in tree['holders']:
flatten_holders_tree(holder, level=level + 1)
for holders_tree in holders_trees:
flatten_holders_tree(holders_tree)
return [reg[k] for k in sorted(reg, key=lambda x: reg[x]['level'] * -1)]
