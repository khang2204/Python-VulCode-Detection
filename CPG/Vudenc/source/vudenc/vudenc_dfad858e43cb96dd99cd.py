from database_writer import get_db
from process_data import processData
from threading import Thread
import logger
import bracket_utils
import constants
import time
from tweet import tweet
analyzed_scenes = False
run_pros = True
should_tweet = True
LOG = logger.logger(__name__)
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
def init(self):...
if not self.testing:
while True:
self.create_analysis_threads()
LOG.info('About to create analyziz threads')
def create_analysis_threads(self):...
self.create_analysis_threads()
self.start_time = time.time()
LOG.info('just finished with analysis threads')
threads = []
time.sleep(constants.SLEEP_TIME)
num_threads = 3
LOG.info('Just finished sleeping')
length = len(self.scenes)
for i in range(num_threads):
i1 = int(length / num_threads * i)
for t in threads:
i2 = int(length / num_threads * (i + 1))
LOG.info('abouto call join for the analysis thread {}'.format(t.name))
LOG.info('we have joined all threads. Should tweet after this')
chunk = self.scenes[i1:i2]
t.join()
if not analyzed_scenes and should_tweet:
name = [scene.get_name() for scene in chunk]
seconds_to_analyze = time.time() - self.start_time
analyzed_scenes = True
def analyze_smashgg(self, urls, name):...
t = Thread(target=self.analyze_scenes, name=str(name), args=(chunk,))
minutes = seconds_to_analyze / 60
seconds_to_analyze = time.time() - self.start_time
LOG.info('we are about to analyze scene {} with {} brackets'.format(name,
    len(urls)))
LOG.info('Trying to start the analysis thread for scenes {}'.format(t.name))
LOG.info('joining for the analysis thread {} in {} minutes'.format(t.name,
    minutes))
minutes = seconds_to_analyze / 60
for url in urls:
t.start()
if not analyzed_scenes and should_tweet:
LOG.info(
    'Just finished analyzing scenes for the first time. It took {} minutes. About to tweet'
    .format(minutes))
sql = "SELECT * FROM analyzed where base_url='{}'".format(url)
def analyze_scenes(self, chunk):...
threads.append(t)
tweet('joining for the analysis thread  {} in {} minutes'.format(t.name,
    minutes))
tweet('Done loading scene data. Took {} minutes'.format(minutes))
res = self.db.exec(sql)
for scene in chunk:
if len(res) == 0:
self.analyze_scene(scene)
def analyze_scene(self, scene):...
display_name = bracket_utils.get_display_base(url)
LOG.info('Skpping pro bracket because it has already been analyzed: {}'.
    format(url))
base_urls = scene.get_base_urls()
if 'doubles' in display_name.lower() or 'dubs' in display_name.lower():
users = scene.get_users()
LOG.info('We are skipping the tournament {} because it is a doubles tournament'
    .format(display_name))
LOG.info('About to process pro bracket {}'.format(url))
name = scene.get_name()
self.data_processor.process(url, name, display_name)
LOG.info('found the following users for scene {}: {}'.format(name, users))
for user in users:
sql = "SELECT * FROM user_analyzed WHERE user='{}';".format(user)
for base_url in base_urls:
results = self.db.exec(sql)
LOG.info('About to start this analysis thread for scene {}'.format(scene.
    get_name()))
if not analyzed_scenes and should_tweet:
if len(results) > 0:
sql = "SELECT first,last FROM valids WHERE base_url = '" + str(base_url) + "';"
tweet('About to start ranking for scene {}'.format(name))
self.data_processor.check_and_update_ranks(name)
most_recent_page = bracket_utils.get_brackets_from_user(user, pages=1)
user_urls = bracket_utils.get_brackets_from_user(user)
result = self.db.exec(sql)
for bracket in most_recent_page:
for url in user_urls:
has_results = len(result) > 0
LOG.info('here are the brackets from the most recent page of user {}: {}'.
    format(user, most_recent_page))
LOG.info('found this url from a user: {} {}'.format(url, user))
LOG.info('done with user {}'.format(user))
if has_results:
sql = "SELECT * FROM user_analyzed WHERE url='{}' AND user='{}';".format(
    bracket, user)
display_name = bracket_utils.get_display_base(url)
LOG.info('validURLs found values in the database' + str(result))
first = bracket_utils._get_first_valid_url(base_url)
results = self.db.exec(sql)
if 'doubles' in display_name.lower() or 'dubs' in display_name.lower():
first = result[0][0]
last = bracket_utils._get_last_valid_url(base_url, first)
if len(results) == 0:
LOG.info('We are skipping the tournament {} because it is a doubles tournament'
    .format(display_name))
self.data_processor.process(url, name, display_name)
last = result[0][1]
sql = 'INSERT INTO valids (base_url, first, last, scene) VALUES ('
LOG.info('found this url from a user: {} {}'.format(bracket, user))
LOG.info('url {} is not new for user {}'.format(bracket, user))
sql = (
    "INSERT INTO user_analyzed (url, user, scene) VALUES ('{}', '{}', '{}');"
    .format(url, user, name))
new_last = bracket_utils._get_last_valid_url(base_url, last - 1)
sql += "'" + str(base_url) + "', " + str(first) + ', ' + str(last
    ) + ", '" + str(name) + "');"
display_name = bracket_utils.get_display_base(bracket)
self.db.exec(sql)
if not new_last == last:
self.db.exec(sql)
if 'doubles' in display_name.lower() or 'dubs' in display_name.lower():
if new_last - last > 5:
for i in range(first, last + 1):
LOG.info('We are skipping the tournament {} because it is a doubles tournament'
    .format(display_name))
self.data_processor.process(bracket, name, display_name)
f.write(
    '[validURLs.py:55]: found a SHIT TON of new tournaments for bracket: {}'
    .format(base_url))
bracket = base_url.replace('###', str(new_last))
bracket = base_url.replace('###', str(i))
sql = (
    "INSERT INTO user_analyzed (url, user, scene) VALUES ('{}', '{}', '{}');"
    .format(bracket, user, name))
sql = 'UPDATE valids SET last=' + str(new_last) + " where base_url = '" + str(
    base_url) + "';"
LOG.info('Found new bracket: {}'.format(bracket))
display_name = bracket_utils.get_display_base(bracket, counter=i)
self.db.exec(sql)
self.db.exec(sql)
msg = 'Found new bracket: {}'.format(bracket)
if 'doubles' in display_name.lower() or 'dubs' in display_name.lower():
msg = 'Found new {} bracket: {}'.format(name, bracket)
for i in range(last + 1, new_last + 1):
tweet(msg)
LOG.info('We are skipping the tournament {} because it is a doubles tournament'
    .format(display_name))
self.data_processor.process(bracket, name, display_name)
tweet(msg)
bracket = base_url.replace('###', str(i))
display_name = bracket_utils.get_display_base(bracket, counter=i)
if 'doubles' in display_name.lower() or 'dubs' in display_name.lower():
LOG.info('We are skipping the tournament {} because it is a doubles tournament'
    .format(display_name))
self.data_processor.process(bracket, name, display_name, new_bracket=True)
