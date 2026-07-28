def get_articles(indices):...
query = cur.mogrify(
    'SELECT * FROM articles WHERE index IN %s ORDER BY last_submitted DESC',
    (tuple(indices),))
cur.execute(query)
articles = cur.fetchall()
return articles
