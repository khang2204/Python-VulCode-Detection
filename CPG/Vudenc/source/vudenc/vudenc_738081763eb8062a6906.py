def _seed_games_and_powers(tournament, the_round):...
"""docstring"""
seeder = _create_game_seeder(tournament, the_round.number())
sitters, two_gamers = _sitters_and_two_gamers(tournament, the_round)
return seeder.seed_games_and_powers(omitting_players=sitters,
    players_doubling_up=two_gamers)
