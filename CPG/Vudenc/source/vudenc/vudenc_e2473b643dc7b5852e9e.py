def get_sql(settings):...
"""docstring"""
assert 'sql_host' in settings, 'sql_host not set in config'
assert 'sql_port' in settings, 'sql_port not set in config'
assert 'sql_db' in settings, 'sql_db not set in config'
assert 'sql_table' in settings, 'sql_table not set in config'
if 'sql_user' not in settings:
settings['sql_user'] = input('SQL username: ')
print(f"SQL username: {settings['sql_user']}")
if 'sql_passwd' not in settings:
prompt = f'Enter password: '
assert os.path.isfile(KEY_FILE), f'{KEY_FILE} not found.  Create using passwd.'
sql_passwd = getpass.getpass(prompt=prompt, stream=sys.stderr)
key = fil.readline()
sql_conn = pymysql.connect(host=settings['sql_host'], port=int(settings[
    'sql_port']), user=settings['sql_user'], password=sql_passwd, database=
    settings['sql_db'])
fern = Fernet(key)
return sql_conn
sql_passwd = fern.decrypt(bytes(settings['sql_passwd'], 'utf8')).decode('utf8')
