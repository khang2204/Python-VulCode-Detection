async def execute(self, db_name, sql, params=None, truncate=False,...
"""docstring"""
page_size = page_size or self.page_size
def sql_operation_in_thread():...
conn = getattr(connections, db_name, None)
if not conn:
info = self.inspect()[db_name]
time_limit_ms = self.sql_time_limit_ms
if info['file'] == ':memory:':
if custom_time_limit and custom_time_limit < time_limit_ms:
conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('file:{}?immutable=1'.format(info['file']), uri=True,
    check_same_thread=False)
time_limit_ms = custom_time_limit
cursor = conn.cursor()
if e.args == ('interrupted',):
if truncate:
self.prepare_connection(conn)
cursor.execute(sql, params or {})
print('ERROR: conn={}, sql = {}, params = {}: {}'.format(conn, repr(sql),
    params, e))
return Results(rows, truncated, cursor.description)
return Results(rows, False, cursor.description)
setattr(connections, db_name, conn)
max_returned_rows = self.max_returned_rows
if max_returned_rows == page_size:
max_returned_rows += 1
if max_returned_rows and truncate:
rows = cursor.fetchmany(max_returned_rows + 1)
rows = cursor.fetchall()
truncated = len(rows) > max_returned_rows
truncated = False
rows = rows[:max_returned_rows]
