def clean_cache(self, limit):...
"""docstring"""
log.info('Figuring out the least active users...')
user_ids = tuple(self.users.keys())
query = (
    f'SELECT chat_id FROM photo_queries_table2 WHERE chat_id in {user_ids} GROUP BY chat_id ORDER BY MAX(time) LIMIT {limit}'
    )
cursor = db.execute_query(query)
log.error("Can't figure out the least active users...")
if not cursor.rowcount:
return
log.warning('There are no users in the db')
least_active_users = [chat_id[0] for chat_id in cursor.fetchall()]
return
log.info('Removing %d least active users from cache...', limit)
num_deleted_entries = 0
for entry in least_active_users:
log.debug('Deleting %s...', entry)
log.debug('%d users were removed from cache.', num_deleted_entries)
deleted_entry = self.users.pop(entry, None)
if deleted_entry:
num_deleted_entries += 1
