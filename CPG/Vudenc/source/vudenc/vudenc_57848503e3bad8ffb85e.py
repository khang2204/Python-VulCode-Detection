def check_and_update_ranks(self, scene):...
LOG.info('About to check if ranks need updating for {}'.format(scene))
sql = 'select count(*) from ranks where scene="{}";'.format(scene)
res = self.db.exec(sql)
count = res[0][0]
n = (5 if scene == 'pro' or scene == 'pro_wiiu' else constants.
    TOURNAMENTS_PER_RANK)
if count == 0:
LOG.info('Detected that we need to bulk update ranks for {}'.format(scene))
sql = ("select date from ranks where scene='{}' order by date desc limit 1;"
    .format(scene))
first_month = bracket_utils.get_first_month(self.db, scene)
res = self.db.exec(sql)
last_month = bracket_utils.get_last_month(self.db, scene)
last_rankings_date = res[0][0]
months = bracket_utils.iter_months(first_month, last_month, include_first=
    False, include_last=True)
more_than_one_month = bracket_utils.has_month_passed(last_rankings_date)
for month in months:
if more_than_one_month:
urls, _ = bracket_utils.get_n_tournaments_before_date(self.db, scene, month, n)
today = datetime.datetime.today().strftime('%Y-%m-%d')
LOG.info(
    'It has not yet been 1 month since we calculated ranks for {}. Skipping'
    .format(scene))
self.process_ranks(scene, urls, month)
msg = 'Detected that we need up update monthly ranks for {}, on {}'.format(
    scene, today)
LOG.info(msg)
if not today.split('-')[-1] == '1':
LOG.exc('We are calculating ranks today, {}, but it isnt the first'.format(
    today))
months = bracket_utils.iter_months(last_rankings_date, today, include_first
    =False, include_last=True)
for month in months:
prev_date = bracket_utils.get_previous_month(month)
brackets_during_month = bracket_utils.get_tournaments_during_month(self.db,
    scene, prev_date)
if len(brackets_during_month) > 0:
tweet('Calculating {} ranks for {}'.format(month, scene))
urls, _ = bracket_utils.get_n_tournaments_before_date(self.db, scene, month, n)
self.process_ranks(scene, urls, month)
