def get_table_dict(table):...
database = sqlite3.connect('app.db')
cur = database.execute('select * from {} order by timestamp desc'.format(table)
    )
columns = [column[0] for column in cur.description]
results = []
for row in cur.fetchall():
results.append(dict(zip(columns, row)))
return results
