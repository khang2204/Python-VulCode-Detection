def insert_result_log(self, qid, hoax, fact, unknown, unrelated, conclusion):...
sql = (
    'INSERT INTO log_result (id_query, finished_at, hoax_score, fact_score, unknown_score, unrelated_score, conclusion) VALUES'
     + "('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (qid, datetime.now(),
    hoax, fact, unknown, unrelated, conclusion))
self.cur.execute(sql)
self.conn.commit()
return self.cur.lastrowid
