async def get_item_list(player_uid: int):...
"""docstring"""
await cursor.execute('SELECT uid, item_id FROM item where player_uid = %d' %
    player_uid)
_error_report(ex)
return datas, True
datas = cursor.fetchall()
return tuple(), False
