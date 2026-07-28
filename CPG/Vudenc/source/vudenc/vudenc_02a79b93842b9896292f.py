def get_number_of_columns_of_phrase_table(self, db_file):...
"""docstring"""
if not path.exists(db_file):
return 0
db = sqlite3.connect(db_file)
return 0
tp_res = db.execute("select sql from sqlite_master where name='phrases';"
    ).fetchall()
str = ' '.join(tp_res[0][0].splitlines())
res = re.match('.*\\((.*)\\)', str)
if res:
tp = res.group(1).split(',')
return 0
return len(tp)
