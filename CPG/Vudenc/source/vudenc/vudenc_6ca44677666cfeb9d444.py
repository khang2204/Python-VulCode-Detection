def scan_git_subtree(tree, path):...
for p in path.strip('/').split('/'):
tree = tree[p]
scan_git_tree(tree)
