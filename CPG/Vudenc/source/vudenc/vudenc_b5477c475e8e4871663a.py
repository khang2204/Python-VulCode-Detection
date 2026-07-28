def create_karma_table():...
db = db_connect()
cursor = db.cursor()
cursor.execute(PEOPLE_TABLE)
db.commit()
logger.info('successfully created karma db for the first time')
