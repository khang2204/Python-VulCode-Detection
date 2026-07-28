def get_article(index):...
query = 'SELECT * FROM articles WHERE index=' + str(index)
cur.execute(query)
article = cur.fetchone()
return article
