def check_tables():...
db = db_connect()
cursor = db.cursor()
cursor.execute("""
            SELECT 1 FROM people LIMIT 1;
            """)
cursor.execute("""
            SELECT 1 FROM people LIMIT 1;
            """)
cursor.fetchone()
cursor.fetchone()
logger.debug('people table exists')
logger.debug('people table exists')
