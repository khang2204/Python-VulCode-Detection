def check_query(self, qhash):...
sql = (
    'INSERT INTO log_query (query_text, query_search, query_hash, query_time, client_ip, client_browser) VALUES'
     + "({}, {}, '{}', '{}', '{}', {})".format(json.dumps(text), json.dumps
    (search), qhash, datetime.now(), ip, json.dumps(browser)))
self.cur.execute(sql)
self.conn.commit()
