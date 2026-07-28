@tornado.gen.coroutine...
sql = (
    'INSERT INTO boiler_room_reports VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    )
assert room_id
assert report_id
params = [room_id, report_id]
for col in boiler_room_report_cols:
params.append(get_safe_val(src, col))
yield tx.execute(query=sql, params=params)
