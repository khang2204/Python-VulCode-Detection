def is_flagged(value, flag):...
if isinstance(value, AnnotatedString):
return flag in value.flags
return False
