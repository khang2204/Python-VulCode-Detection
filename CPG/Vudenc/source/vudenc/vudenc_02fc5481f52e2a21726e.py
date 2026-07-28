@staticmethod...
"""docstring"""
log.info(
    'Evaluating last active users with date of last time when they used bot...'
    )
query = (
    f'SELECT p.chat_id, u.first_name, u.nickname, u.last_name, u.language FROM photo_queries_table2 p INNER JOIN users u ON p.chat_id = u.chat_id GROUP BY u.chat_id, u.first_name, u.nickname, u.last_name, u.language ORDER BY MAX(time)DESC LIMIT {limit}'
    )
cursor = db.execute_query(query)
log.error(
    'Cannot get the last active users because of some problems with the database'
    )
last_active_users = cursor.fetchall()
return last_active_users
