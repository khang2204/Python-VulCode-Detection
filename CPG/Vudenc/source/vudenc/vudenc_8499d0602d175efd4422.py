def scrub_custom_query(query, key, txt):...
if '%(key)s' in query:
query = query.replace('%(key)s', key)
if '%s' in query:
query = query.replace('%s', (txt or '') + '%')
return query
