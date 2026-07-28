def create_also_table():...
db = db_connect()
cursor = db.cursor()
cursor.execute(ALSO_TABLE)
db.commit()
logger.info('successfully created also table for the first time')
