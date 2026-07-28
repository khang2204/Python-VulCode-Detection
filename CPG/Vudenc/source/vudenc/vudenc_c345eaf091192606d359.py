async def update_hp(name: str, hp: int):...
"""docstring"""
await cursor.execute("UPDATE player SET hp=%d where name = '%s'" % (hp, name))
_error_report(ex)
await conn.commit()
return False
return True
