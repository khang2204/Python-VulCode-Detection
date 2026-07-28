def get_database_desc(self, db_file):...
if not path.exists(db_file):
return None
db = sqlite3.connect(db_file)
return None
desc = {}
for row in db.execute('SELECT * FROM desc;').fetchall():
desc[row[0]] = row[1]
return desc
