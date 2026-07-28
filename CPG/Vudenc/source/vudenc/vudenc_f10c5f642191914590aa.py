def init_db():...
"""docstring"""
db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=
    sys.argv[2], db=sys.argv[3])
return db
