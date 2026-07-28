def _sitters_and_two_gamers(tournament, the_round):...
"""docstring"""
tourney_players = tournament.tournamentplayer_set.all()
round_players = the_round.roundplayer_set.all()
rps = []
sitters = set()
two_gamers = set()
for rp in round_players:
assert rp.gameplayers().count(
    ) == 0, '%d games already exist for %s in this round' % (rp.gameplayers
    ().count(), str(rp))
assert not sitters or not two_gamers
rps.append(rp)
if sitters:
if rp.game_count == 1:
assert (len(rps) - len(sitters)) % 7 == 0
if two_gamers:
if rp.game_count == 0:
assert (len(rps) + len(two_gamers)) % 7 == 0
for tp in tourney_players:
sitters.add(rp.tournamentplayer())
if rp.game_count == 2:
if not round_players.filter(player=tp.player).exists():
return sitters, two_gamers
two_gamers.add(rp.tournamentplayer())
assert 0, 'Unexpected game_count value %d for %s' % (rp.game_count, str(rp))
sitters.add(tp)
