def get_top_articles(list_count):...
"""docstring"""
query = (
    'select a.title, count(alv.article) as views from articles a,  article_log_view alv where a.slug = alv.article  group by a.title  order by count(alv.article) desc limit %d;'
     % list_count)
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute(query)
rows = c.fetchall()
db.close()
return rows
