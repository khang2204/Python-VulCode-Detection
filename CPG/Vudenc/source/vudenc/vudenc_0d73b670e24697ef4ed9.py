def format_match(match):...
name = match.group('name')
value = wildcards[name]
if keep_dynamic:
if fail_dynamic and value == dynamic_fill:
return '{{{}}}'.format(name)
if fill_missing:
return str(value)
return dynamic_fill
