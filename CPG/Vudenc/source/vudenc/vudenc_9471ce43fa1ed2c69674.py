def escape_col(col):...
if not col:
return col
if ESCAPE_RE.match(col):
return col
return u'{}`{}`'.format(*NEGATE_RE.match(col).groups())
