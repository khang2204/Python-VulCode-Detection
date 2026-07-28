@classmethod...
"""docstring"""
pony_query = cls.get_entries_query(**kwargs)
if isinstance(metadata_type, list):
pony_query = pony_query.where(lambda g: g.metadata_type in metadata_type)
pony_query = pony_query.where(metadata_type=metadata_type)
if exclude_deleted:
pony_query = pony_query.where(lambda g: g.status != TODELETE)
if hide_xxx:
pony_query = pony_query.where(lambda g: g.xxx == 0)
if channel_pk:
pony_query = pony_query.where(public_key=channel_pk)
count = pony_query.count()
return pony_query[(first or 1) - 1:last
    ] if first or last else pony_query, count
