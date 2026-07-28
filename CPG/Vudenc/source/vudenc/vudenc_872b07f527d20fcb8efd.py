async def get_player_info(name: str) ->tuple:...
"""docstring"""
await cursor.execute(
    "SELECT uid, name, password, lv, xp, hp FROM player where name = '%s'" %
    name)
_error_report(ex)
if data is None:
data = cursor.fetchone()
return tuple()
return tuple()
return data
