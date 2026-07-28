def updateAnswer(database, q_id, answer, update_type):...
"""docstring"""
conn = dbConnect(database)
curs = conn.cursor(MySQLdb.cursors.DictCursor)
statement = 'SELECT * FROM questions WHERE id=' + q_id
curs.execute(statement)
row = curs.fetchone()
timestamp = row['ts']
if update_type == 'publish':
statement = (
    "update questions set status='completed', answer=%s, ts=%s where id=%s")
if update_type == 'save':
statement = (
    "update questions set status='in-progress', answer=%s, ts=%s where id=%s")
curs.execute(statement, (answer, timestamp, q_id))
