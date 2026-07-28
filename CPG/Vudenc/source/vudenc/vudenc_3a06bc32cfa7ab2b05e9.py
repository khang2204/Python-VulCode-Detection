def get_top_authors():...
"""docstring"""
query = (
    'select au.name, count(alv.article) as views  from articles a inner join article_log_view alv  on a.slug = alv.article  inner join authors au  on a.author = au.id  group by au.name  order by count(alv.article) desc;'
    )
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute(query)
rows = c.fetchall()
db.close()
return rows
