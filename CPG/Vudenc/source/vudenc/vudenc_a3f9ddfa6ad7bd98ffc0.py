import logger
import datetime
import constants
import get_results
import time
import copy
import player_web
import bracket_utils
from get_ranks import get_ranks
from get_results import get_coalesced_tag, sanitize_tag
import re
from tweet import tweet
LOG = logger.logger(__name__)
def __init__(self, db):...
LOG.info('loading constants for process')
self.db = db
def process(self, bracket, scene, display_name, new_bracket=False):...
sql = "SELECT * FROM analyzed WHERE base_url = '" + str(bracket) + "';"
result = self.db.exec(sql)
if len(result) > 0:
LOG.info('tried to analyze {}, but has already been done.'.format(bracket))
if 'smash.gg' in bracket:
return
success = get_results.process(bracket, scene, self.db, display_name)
html, status = bracket_utils.hit_url(bracket)
if success:
if status == 200 and bracket_utils.is_valid(html):
self.insert_placing_data(bracket, new_bracket)
LOG.exc('Analyzing smashgg tournament {} was not successful'.format(bracket))
get_results.process(bracket, scene, self.db, display_name)
def insert_placing_data(self, bracket, new_bracket):...
self.insert_placing_data(bracket, new_bracket)
LOG.info('we have called insert placing data on bracket {}'.format(bracket))
tournament_placings = bracket_utils.get_tournament_placings(bracket)
for player, placing in tournament_placings.items():
player = sanitize_tag(player)
LOG.info('tournament placings for {} are {}'.format(bracket,
    tournament_placings))
player = get_coalesced_tag(player)
def check_and_update_ranks(self, scene):...
sql = ('INSERT INTO placings (url, player, place) VALUES ' +
    " ('{}', '{}', '{}')".format(bracket, player, placing))
LOG.info('About to check if ranks need updating for {}'.format(scene))
self.db.exec(sql)
sql = 'select count(*) from ranks where scene="{}";'.format(scene)
if 'christmasmike' == player and new_bracket:
res = self.db.exec(sql)
if placing < 10:
count = res[0][0]
msg = "Congrats on making {} dude! You're the best.".format(placing)
n = (5 if scene == 'pro' or scene == 'pro_wiiu' else constants.
    TOURNAMENTS_PER_RANK)
tweet(msg)
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
def process_ranks(self, scene, urls, recent_date):...
today = datetime.datetime.today().strftime('%Y-%m-%d')
LOG.info(
    'It has not yet been 1 month since we calculated ranks for {}. Skipping'
    .format(scene))
self.process_ranks(scene, urls, month)
PLAYER1 = 0
msg = 'Detected that we need up update monthly ranks for {}, on {}'.format(
    scene, today)
PLAYER2 = 1
LOG.info(msg)
WINNER = 2
if not today.split('-')[-1] == '1':
DATE = 3
LOG.exc('We are calculating ranks today, {}, but it isnt the first'.format(
    today))
months = bracket_utils.iter_months(last_rankings_date, today, include_first
    =False, include_last=True)
SCENE = 4
for month in months:
sql = "SELECT * FROM ranks WHERE scene = '{}' AND date='{}';".format(str(
    scene), recent_date)
prev_date = bracket_utils.get_previous_month(month)
res = self.db.exec(sql)
brackets_during_month = bracket_utils.get_tournaments_during_month(self.db,
    scene, prev_date)
if len(res) > 0:
if len(brackets_during_month) > 0:
LOG.info('We have already calculated ranks for {} on date {}. SKipping'.
    format(scene, recent_date))
matches = bracket_utils.get_matches_from_urls(self.db, urls)
tweet('Calculating {} ranks for {}'.format(month, scene))
return
LOG.info('About to start processing ranks for scene {} on {}'.format(scene,
    recent_date))
urls, _ = bracket_utils.get_n_tournaments_before_date(self.db, scene, month, n)
win_loss_dict = {}
self.process_ranks(scene, urls, month)
for match in matches:
p1 = match[PLAYER1]
ranks = get_ranks(win_loss_dict)
p2 = match[PLAYER2]
tag_rank_map = {}
winner = match[WINNER]
for i, x in enumerate(ranks):
date = match[DATE]
points, player = x
player_web.update_ranks(tag_rank_map)
if p1 not in win_loss_dict:
rank = len(ranks) - i
win_loss_dict[p1] = {}
if p2 not in win_loss_dict[p1]:
sql = (
    "INSERT INTO ranks (scene, player, rank, points, date) VALUES ('{}', '{}', '{}', '{}', '{}');"
    .format(str(scene), str(player), int(rank), str(points), str(recent_date)))
win_loss_dict[p1][p2] = []
win_loss_dict[p1][p2].append((date, winner == p1))
self.db.exec(sql)
if p2 not in win_loss_dict:
sql = "SELECT scene FROM players WHERE tag='{}';".format(player)
win_loss_dict[p2] = {}
if p1 not in win_loss_dict[p2]:
res = self.db.exec(sql)
win_loss_dict[p2][p1] = []
win_loss_dict[p2][p1].append((date, winner == p2))
if len(res) == 0 or res[0][0] == scene:
map = {'rank': rank, 'total_ranked': len(ranks)}
tag_rank_map[player] = map
