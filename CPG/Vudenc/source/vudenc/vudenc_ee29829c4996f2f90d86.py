def has_read_perm(user, group, is_member, is_private):...
"""docstring"""
if group is None or is_member is None or is_member(user, group):
return True
if is_private is not None and is_private(group):
return False
return True
