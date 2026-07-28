def get_reference_by_qhash(self, qhash):...
sql = "SELECT * FROM article_reference WHERE query_hash = '%s'" % qhash
self.cur.execute(sql)
self.conn.commit()
articles = []
if self.cur.rowcount > 0:
for row in self.cur.fetchall():
return articles
article = {}
article['hash'] = row['article_hash']
article['date'] = row['article_date']
article['url'] = row['article_url']
article['content'] = row['article_content']
articles.append(article)
