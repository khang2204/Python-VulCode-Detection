def is_reference_exist(self, ahash):...
sql = "SELECT id FROM article_reference WHERE article_hash = '%s'" % ahash
self.cur.execute(sql)
self.conn.commit()
return self.cur.rowcount == 1
