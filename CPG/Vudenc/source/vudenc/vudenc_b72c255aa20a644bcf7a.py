def get_descendant_ids(node):...
children = node['children']
if children:
return itertools.chain.from_iterable([get_descendant_ids(child) for child in
    children])
return node['id'],
