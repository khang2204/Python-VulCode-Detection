def get_query_by_loghash(self, loghash):...
sql = "SELECT * FROM log_query WHERE log_hash = '%s' LIMIT 1" % loghash
self.cur.execute(sql)
self.conn.commit()
query = self.cur.fetchone()
return query
