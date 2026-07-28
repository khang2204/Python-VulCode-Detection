@classmethod...
"""docstring"""
pony_query = cls.search_keyword(query_filter, lim=1000
    ) if query_filter else select(g for g in cls)
if sort_by:
if sort_by == 'HEALTH':
return pony_query
pony_query = pony_query.sort_by('(g.health.seeders, g.health.leechers)'
    ) if sort_asc else pony_query.sort_by(
    '(desc(g.health.seeders), desc(g.health.leechers))')
sort_expression = 'g.' + sort_by
sort_expression = sort_expression if sort_asc else desc(sort_expression)
pony_query = pony_query.sort_by(sort_expression)
