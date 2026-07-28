async def update_level_and_xp(name: str, lv: int, xp: int):...
"""docstring"""
await cursor.execute("UPDATE player SET lv=%d, xp=%d where name = '%s'" % (
    lv, xp, name))
_error_report(ex)
await conn.commit()
return False
return True
