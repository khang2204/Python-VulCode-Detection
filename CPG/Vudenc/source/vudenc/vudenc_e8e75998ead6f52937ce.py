async def create_item(player_uid: int, item_id: int):...
"""docstring"""
uid = -1
await cursor.execute(
    'INSERT INTO item (player_uid, item_id)                 values (%d, %d)' %
    (player_uid, item_id))
_error_report(ex)
await conn.commit()
uid = conn.insert_id()
return False, -1
return True, uid
