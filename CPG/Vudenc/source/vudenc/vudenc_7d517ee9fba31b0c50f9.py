def dynamic(value):...
"""docstring"""
annotated = flag(value, 'dynamic')
tocheck = [annotated] if not_iterable(annotated) else annotated
for file in tocheck:
matches = list(_wildcard_regex.finditer(file))
return annotated
for match in matches:
if match.group('constraint'):
