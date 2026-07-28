def get_articles_by_subject(subject):...
query = ("SELECT * FROM articles WHERE subject='" + subject +
    "' ORDER BY last_submitted DESC")
cur.execute(query)
articles = cur.fetchall()
return articles
