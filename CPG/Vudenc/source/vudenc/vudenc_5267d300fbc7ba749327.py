def add_tag(self, name):...
"""docstring"""
cur = self.__con.cursor()
cur.execute("INSERT INTO tags(name) VALUE('%s')" % name)
return Database.DUPLICATE
return Database.SUCCESS
