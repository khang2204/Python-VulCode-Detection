def to_fts_query(text):...
if not text:
return ''
words = text.split(' ')
query_list = [(u'"' + sanitize_for_fts(word) + u'"*') for word in words]
return ' AND '.join(query_list)
