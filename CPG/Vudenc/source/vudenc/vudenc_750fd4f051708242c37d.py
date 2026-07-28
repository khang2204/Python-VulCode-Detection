def apply_wildcards(pattern, wildcards, fill_missing=False, fail_dynamic=...
def format_match(match):...
name = match.group('name')
value = wildcards[name]
if keep_dynamic:
return re.sub(_wildcard_regex, format_match, pattern)
if fail_dynamic and value == dynamic_fill:
return '{{{}}}'.format(name)
if fill_missing:
return str(value)
return dynamic_fill
