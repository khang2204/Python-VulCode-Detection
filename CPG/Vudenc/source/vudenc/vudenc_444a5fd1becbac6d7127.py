def dbConnect(database):...
"""docstring"""
dsn = dbconn2.read_cnf('/students/' + USER + '/.my.cnf')
dsn['db'] = database
conn = dbconn2.connect(dsn)
return conn
