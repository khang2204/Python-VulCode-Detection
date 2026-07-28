def get_database_connection():...
"""docstring"""
connection = getattr(g, 'database', None)
if connection is None:
g.database = sqlite3.connect(DATABASE_FILE)
return connection
connection = g.database
connection.row_factory = sqlite3.Row
