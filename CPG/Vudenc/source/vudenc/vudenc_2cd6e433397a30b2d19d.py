@staticmethod...
"""docstring"""
checked_tags = []
for tag in tags:
if tag:
return checked_tags
tag = str(tag).strip()
checked_tags.append(tag)
log.info('Looking up collation for %s', tag)
query = 'SELECT right_tag FROM tag_table WHERE wrong_tag="{}"'.format(tag)
cursor = db.execute_query(query)
if not cursor:
log.error("Can't check the tag because of the db error")
if cursor.rowcount:
log.warning('Tag will stay as is.')
tag = cursor.fetchone()[0]
log.info('Tag after looking up in tag_tables - %s.', tag)
