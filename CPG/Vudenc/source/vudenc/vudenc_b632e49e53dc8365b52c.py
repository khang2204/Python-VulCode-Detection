@classmethod...
if not query or query == '*':
return []
fts_ids = raw_sql(
    'SELECT rowid FROM FtsIndex WHERE FtsIndex MATCH $query ORDER BY bm25(FtsIndex) LIMIT $lim'
    )
return cls.select(lambda g: g.rowid in fts_ids)
