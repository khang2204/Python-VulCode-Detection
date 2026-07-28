def sid_is_valid(sid):...
"""docstring"""
if '/' in sid or '\\' in sid:
return False
if len(sid) >= 10:
return False
return True
