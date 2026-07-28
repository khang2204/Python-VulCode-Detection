def insert_reference_feedback(self, ahash, is_relevant, reason, label, ip,...
print(str(ahash))
print(str(is_relevant))
sql = (
    'INSERT INTO feedback_reference (article_hash, reported_at, is_relevant, reason, feedback_label, client_ip, client_browser) VALUES'
     + "('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (ahash, datetime.now(
    ), is_relevant, reason, label, ip, browser))
self.cur.execute(sql)
self.conn.commit()
return self.cur.lastrowid
