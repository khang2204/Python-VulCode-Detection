async def get_table_definition(self, database_name, table, type_='table'):...
table_definition_rows = list(await self.execute(database_name,
    'select sql from sqlite_master where name = :n and type=:t', {'n':
    table, 't': type_}))
if not table_definition_rows:
return None
return table_definition_rows[0][0]
