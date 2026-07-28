def insert_placing_data(self, bracket, new_bracket):...
LOG.info('we have called insert placing data on bracket {}'.format(bracket))
tournament_placings = bracket_utils.get_tournament_placings(bracket)
for player, placing in tournament_placings.items():
player = sanitize_tag(player)
LOG.info('tournament placings for {} are {}'.format(bracket,
    tournament_placings))
player = get_coalesced_tag(player)
sql = ('INSERT INTO placings (url, player, place) VALUES ' +
    " ('{}', '{}', '{}')".format(bracket, player, placing))
self.db.exec(sql)
if 'christmasmike' == player and new_bracket:
if placing < 10:
msg = "Congrats on making {} dude! You're the best.".format(placing)
tweet(msg)
