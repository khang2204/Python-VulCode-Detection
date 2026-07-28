def _parse_marc_code(field):...
"""docstring"""
field = str(field)
if len(field) < 4:
field += '__'
tag = field[0:3]
ind1 = field[3].replace('_', '')
ind2 = field[4].replace('_', '')
return tag, ind1, ind2
