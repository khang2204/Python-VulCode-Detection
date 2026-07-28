def dbtables_to_csv():...
table_names = conn.cursor().execute(
    "SELECT name FROM sqlite_master WHERE type='table';").fetchall()
table_names = [x[0] for x in table_names]
open_query = 'SELECT * FROM {}'
for table in table_names:
pd.read_sql(open_query.format(table), conn).to_csv('{}.csv'.format(table),
    index=False)
