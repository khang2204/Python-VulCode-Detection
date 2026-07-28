def reportMatch(winner, loser):...
"""docstring"""
winner = bleach.clean(str(winner))
loser = bleach.clean(str(loser))
execute('insert into Match(winner, loser) values(%s, %s)', (winner, loser))
