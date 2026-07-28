def iterate_fsnode(node):...
for item in node.sub_items:
if item.parent:
return
item.parent = node
iterate_fsnode(item)
