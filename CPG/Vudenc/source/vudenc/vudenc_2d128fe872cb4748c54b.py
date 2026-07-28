def insert_query_log(self, lhash, text, search, qhash, ip, browser):...
sql = (
    'INSERT INTO log_query (log_hash, query_text, query_search, query_hash, query_time, client_ip, client_browser, clicked) VALUES'
     + "({}, {}, {}, '{}', '{}', '{}', {}, {})".format(json.dumps(lhash),
    json.dumps(text), json.dumps(search), qhash, datetime.now(), ip, json.
    dumps(browser), 0))
self.cur.execute(sql)
self.conn.commit()
return self.cur.lastrowid
