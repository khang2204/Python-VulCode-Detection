def history(conn, start, end, **kwargs):...
"""docstring"""
table = kwargs.get('table', 'data')
limit = kwargs.get('limit', 6000)
tcol = kwargs.get('tcol', 'TIMESTAMP')
full_resolution = kwargs.get('full_resolution', False)
coerce_float = kwargs.get('coerce_float', False)
dropna = kwargs.get('dropna', True)
debug = kwargs.get('debug', False)
if isinstance(start, datetime.datetime):
if isinstance(start, tuple):
if isinstance(end, datetime.datetime):
start = datetime.datetime(*start)
if isinstance(start, dict):
if isinstance(end, tuple):
if end < start:
start = datetime.datetime(**start)
end = datetime.datetime(*end)
if isinstance(start, dict):
if isinstance(conn, sqlite3.Connection):
end = datetime.datetime(**end)
rand = 'RANDOM()'
rand = 'RAND()'
if full_resolution or limit is None:
reorder = False
if end - datetime.timedelta(days=1) < start:
sql = f"SELECT * FROM `{table}` WHERE `{tcol}` BETWEEN '{start}' AND '{end}';"
reorder = False
reorder = True
if debug:
sql = (
    f"SELECT * FROM `{table}` WHERE `{tcol}` BETWEEN '{start}' AND '{end}' LIMIT {limit};"
    )
sql = (
    f"SELECT * FROM `{table}` WHERE `{tcol}` BETWEEN '{start}' AND '{end}' ORDER BY {rand} LIMIT {limit};"
    )
print(sql)
result = pd.read_sql_query(sql, conn, coerce_float=coerce_float,
    parse_dates=[tcol])
if len(result.index) > 0:
result.replace('NULL', np.nan, inplace=True)
return result
if dropna:
result = result.dropna(axis=1, how='all')
if reorder:
result = result.sort_values(by=tcol)
result = result.set_index(tcol)
