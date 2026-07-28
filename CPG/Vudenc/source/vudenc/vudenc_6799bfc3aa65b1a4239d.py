def get_query_log(self):...
sql = 'SELECT * FROM log_query ORDER BY query_time DESC'
self.cur.execute(sql)
self.conn.commit()
queries = []
for row in self.cur.fetchall():
query = {}
return queries
query['log_hash'] = row['log_hash']
query['query_text'] = row['query_text']
query['query_search'] = row['query_search']
query['query_hash'] = row['query_hash']
query['query_time'] = str(row['query_time'])
query['client_ip'] = row['client_ip']
query['client_browser'] = row['client_browser']
query['clicked'] = row['clicked']
queries.append(query)
