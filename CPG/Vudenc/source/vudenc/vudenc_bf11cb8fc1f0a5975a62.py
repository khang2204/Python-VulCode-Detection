def bracket_complete(data):...
if 'player1' not in data.lower() and 'player2' not in data.lower():
if debug:
if '"player1":null' in data.lower() or '"player2":null' in data.lower():
print('didnt find any players, must be invalid')
return False
if debug:
return True
print('found a null player, must be invalid')
return False
