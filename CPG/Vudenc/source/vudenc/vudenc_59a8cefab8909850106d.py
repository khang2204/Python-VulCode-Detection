async def create_account(name: str, password: str):...
"""docstring"""
uid = -1
await cursor.execute(
    "INSERT INTO player (name, password, lv, xp, hp) values ('%s', '%s', 1, 0, 150)"
     % (name, password))
await conn.rollback()
await conn.commit()
uid = conn.insert_id()
_error_report(ex)
return True, uid
return False, -1
