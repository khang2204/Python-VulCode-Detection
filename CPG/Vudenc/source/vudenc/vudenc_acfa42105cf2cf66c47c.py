def run(config, instrum, wait, output=False, sql=False, header=True, quiet=...
"""docstring"""
tty = sys.stdout.isatty()
settings = parse_settings(config, instrum)
columns = get_columns(settings)
if debug and tty:
print('DEBUG enabled')
device = get_device(settings, instrum, debug=debug)
if tty and not quiet:
device.close()
db = None
print("""
Stopping emonitor.""")
if db is not None:
if output:
db.close()
if sql_conn is not None:
db = get_sqlite(settings, columns)
sql_conn = None
sql_conn.close()
if sql:
sql_conn = get_sql(settings)
if tty:
if not quiet:
if header:
print('Starting emonitor. Use Ctrl-C to stop. \n')
while True:
print(','.join(columns))
if header:
values = tuple(device.read_data())
test = tuple(device.read_data())
is_null = all([(isinstance(v, str) and v.upper() == 'NULL') for v in values])
if debug:
if not is_null:
print(test)
str_width = len(str(test[0]))
values = (time.strftime('%Y-%m-%d %H:%M:%S'),) + values
time.sleep(wait)
print(columns[0].rjust(19) + ' \t', '\t '.join([col.rjust(str_width) for
    col in columns[1:]]))
if tty:
if not quiet:
print(','.join(values))
print('\t '.join(values))
if output:
db_insert(db, TABLE, columns, values, debug=debug)
if sql:
if not sql_conn.open:
warnings.warn('SQL connection failed')
sql_conn.connect()
db_insert(sql_conn, settings['sql_table'], columns, values, debug=debug)
