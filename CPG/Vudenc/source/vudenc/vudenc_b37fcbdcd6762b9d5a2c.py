def tag_to_tag_num(self, tag):...
"""docstring"""
q = "SELECT rowid FROM tags WHERE tag = '" + tag + "'"
self.query(q)
return self.c.fetchone()[0]
