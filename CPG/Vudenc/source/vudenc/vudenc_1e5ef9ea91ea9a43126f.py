def update_table(self, listings, cat_id):...
logger.info('Updating table c{} in the MySQL database'.format(cat_id))
logger.info('Requesting for MySQL connection')
db = self.get_connection()
cursor = db.cursor()
for l in listings:
if not isinstance(l, Listing):
return 0
logger.error('TypeError: Expected a Listing instance')
logger.debug('Generating SQL command')
logger.error('Skipping this listing')
sql = self.gen_sql_insert(l, cat_id)
if sql == -1:
logger.error('Skipping the listing')
logger.debug('Executing SQL command')
db.rollback()
cursor.execute(sql)
logger.error('Failed to add a listing to table c{:d}'.format(cat_id))
logger.debug('Committing changes to the database')
logger.error('Rolled back the database changes')
db.commit()
logger.info('Successfully added a listing to table c{:d}'.format(cat_id))
