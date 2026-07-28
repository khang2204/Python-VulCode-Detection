def _create_game_seeder(tournament, round_number):...
"""docstring"""
tourney_players = tournament.tournamentplayer_set.all()
seeder = GameSeeder(GreatPower.objects.all(), starts=100, iterations=10)
for tp in tourney_players:
seeder.add_player(tp)
for n in range(1, round_number):
rnd = tournament.round_numbered(n)
for tp in tourney_players:
for g in rnd.game_set.all():
for sb in tp.seederbias_set.all():
return seeder
game = set()
seeder.add_bias(sb.player1, sb.player2, sb.weight)
for gp in g.gameplayer_set.all():
game.add((gp.tournamentplayer(), gp.power))
assert len(game) == 7
seeder.add_played_game(game)
