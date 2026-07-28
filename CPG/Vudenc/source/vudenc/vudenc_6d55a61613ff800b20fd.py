def create_task(self, description, tag=None, due_date=None):...
"""docstring"""
cols = {'description': description}
if not tag:
tag = self.default_tag
if due_date:
valid_date = Database.__format_date(due_date)
cur = self.__con.cursor()
if valid_date == Database.INVALID_DATE:
if cur.execute("SELECT tagid FROM tags WHERE name='%s'" % tag):
return valid_date
cols['due_date'] = valid_date
cols['tagid'] = str(cur.fetchone()[0])
self.add_tag(tag)
cur.execute("INSERT INTO tasks(%s) VALUES('%s')" % (','.join(cols.keys()),
    "','".join(cols.values())))
return Database.DUPLICATE
cols['tagid'] = str(self.__con.insert_id())
return Database.SUCCESS
