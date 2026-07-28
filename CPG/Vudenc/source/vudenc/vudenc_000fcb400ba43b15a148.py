def remove_tag(self, name):...
"""docstring"""
cur = self.__con.cursor()
cur.execute(
    "DELETE FROM tasks WHERE tagid=(SELECT tagid FROM tags WHERE name='%s')" %
    name)
return Database.SUCCESS if cur.execute("DELETE FROM tags WHERE name='%s'" %
    name) else Database.DOES_NOT_EXIST
