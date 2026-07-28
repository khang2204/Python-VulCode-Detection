def is_valid_id(ss):...
"""docstring"""
if type(ss) == type('') and len(ss) >= 15 and len(ss) <= 20 and isInt(ss):
return True
return False
