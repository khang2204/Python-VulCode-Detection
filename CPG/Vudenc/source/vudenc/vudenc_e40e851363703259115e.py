def format_tree(tree):...
"""docstring"""
result = [tree['name']]
holders = tree['holders']
for holder_no, holder in enumerate(holders):
spacer_style = spacers[min(len(holders) - (holder_no + 1), 1)]
return result
subtree_lines = format_tree(holder)
for line_no, line in enumerate(subtree_lines):
result.append(spacer_style[min(line_no, 1)] + line)
