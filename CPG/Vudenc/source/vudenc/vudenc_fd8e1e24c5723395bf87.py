@staticmethod...
"""docstring"""
query = 'SELECT COUNT(*) FROM users'
cursor = db.execute_query(query)
log.error("Can't count the total number of users!")
return cursor.fetchone()[0]
