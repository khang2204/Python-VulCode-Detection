def insert_result_feedback(self, qhash, is_know, reason, label, ip, browser):...
sql = (
    'INSERT INTO feedback_result (query_hash, reported_at, is_know, reason, feedback_label, client_ip, client_browser) VALUES'
     + "('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (qhash, datetime.now(
    ), is_know, reason, label, ip, browser))
self.cur.execute(sql)
self.conn.commit()
return self.cur.lastrowid
