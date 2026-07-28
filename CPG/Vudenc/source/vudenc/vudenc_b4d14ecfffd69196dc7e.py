def _is_query(field):...
if re.compile('^(select|delete|update|drop|create)\\s').match(field):
_raise_exception()
if re.compile('\\s*[a-zA-z]*\\s*( from | group by | order by | where | join )'
_raise_exception()
