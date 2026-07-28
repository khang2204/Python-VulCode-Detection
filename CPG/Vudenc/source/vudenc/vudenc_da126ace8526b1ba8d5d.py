async def _clean_tables(app):...
for sa_model in tables.Base.__subclasses__():
table = sa_model.__table__
conn.execute(table.delete())
