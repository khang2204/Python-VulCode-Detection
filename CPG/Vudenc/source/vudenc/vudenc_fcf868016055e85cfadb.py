@cache_number_users_with_same_feature...
"""docstring"""
log.debug('Check how many users also have this feature: %s...', feature)
query = ("SELECT DISTINCT chat_id FROM photo_queries_table2 WHERE {}='{}'".
    format(feature_type, feature))
cursor = db.execute_query(query)
log.error('Cannot check how many users also have this feature: %s...', feature)
if not cursor.rowcount:
return None
log.debug('There were no users with %s...', feature)
log.debug('There is %d users with %s', cursor.rowcount, feature)
return None
return cursor.rowcount - 1
