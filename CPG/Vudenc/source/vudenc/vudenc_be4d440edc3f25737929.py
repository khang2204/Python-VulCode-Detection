def _build_child_key(child_branch=None, child_leaf=None):...
args = [child_leaf, child_branch]
if not any(args) or all(args):
if child_leaf:
branch_part = 'child_leaf'
branch_part = 'child_branch'
id_part = child_leaf
id_part = child_branch
return '{branch_part}_{id_part}'.format(**locals())
