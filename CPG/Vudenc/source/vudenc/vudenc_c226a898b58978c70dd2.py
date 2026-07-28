def create_connection_and_set_cursor(database):...
"""docstring"""
conn = sqlite3.connect(database)
logging.error(e)
cursor = conn.cursor()
sys.exit('No database connection could be established.')
return conn, cursor
