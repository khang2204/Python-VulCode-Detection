def insert_references(self, qid, articles):...
insert_values = []
for article in articles:
insert_values.append((qid, str(article['qhash']), str(article['hash']), str
    (article['date']), str(article['url']), article['content'], datetime.now())
    )
sql = (
    'INSERT INTO article_reference (id_query, query_hash, article_hash, article_date, article_url, article_content, retrieved_at) VALUES'
     + ','.join('(%s, %s, %s, %s, %s, %s, %s)' for _ in insert_values))
flattened_values = [item for sublist in insert_values for item in sublist]
self.cur.execute(sql, flattened_values)
self.conn.commit()
