def del_reference_by_qhash(self, qhash):...
sql = "DELETE FROM article_reference WHERE query_hash = '%s'" % qhash
self.cur.execute(sql)
self.conn.commit()
