def get_sqlite(settings, columns):...
"""docstring"""
assert 'db' in settings, '`db` not set in config'
name = settings['db']
fname, _ = os.path.splitext(name)
fname += '.db'
fil = os.path.join(DATA_DIRE, fname)
if not os.path.isfile(fil):
db = sqlite3.connect(fil)
db_check(db, TABLE, columns)
return db
