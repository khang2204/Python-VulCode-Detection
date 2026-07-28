def flag(value, flag_type, flag_value=True):...
if isinstance(value, AnnotatedString):
value.flags[flag_type] = flag_value
if not_iterable(value):
return value
value = AnnotatedString(value)
return [flag(v, flag_type, flag_value=flag_value) for v in value]
value.flags[flag_type] = flag_value
return value
