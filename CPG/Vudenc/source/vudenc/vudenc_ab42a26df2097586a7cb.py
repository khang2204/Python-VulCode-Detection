def analyze_scene(self, scene):...
base_urls = scene.get_base_urls()
users = scene.get_users()
name = scene.get_name()
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
