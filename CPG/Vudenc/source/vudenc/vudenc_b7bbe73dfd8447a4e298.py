def is_query_exist(self, loghash):...
sql = "SELECT id FROM log_query WHERE log_hash = '%s'" % loghash
self.cur.execute(sql)
self.conn.commit()
return self.cur.rowcount == 1
