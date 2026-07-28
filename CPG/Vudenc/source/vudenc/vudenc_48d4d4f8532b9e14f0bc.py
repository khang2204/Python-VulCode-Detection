@atomic...
"""docstring"""
fs_repo_root = self.get_repo_root()
branches = self.get_branches(fs_repo_root)
if not self.quiet:
print('\n'.join(branches))
return branches
