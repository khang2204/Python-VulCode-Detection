def __init__(self, scenes, testing=False, db_name='smash'):...
self.start_time = time.time()
self.testing = testing
self.scenes = scenes
db_name = 'smash_test' if testing else db_name
self.db = get_db(db=db_name)
sql = 'SELECT count(*) FROM matches'
res = self.db.exec(sql)
if res[0][0] == 0:
should_tweet = True
self.data_processor = processData(self.db)
LOG.info('validURL being created')
