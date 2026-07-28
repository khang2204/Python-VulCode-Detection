def has_write_perm(user, group, is_member):...
"""docstring"""
if group is None or is_member is None or is_member(user, group):
return True
return False
