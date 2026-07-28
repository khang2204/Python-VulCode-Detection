import psycopg2
def get_top_articles(cur, order, limit):...
"""docstring"""
query = (
    """SELECT articles.title, COUNT(*) as views
            FROM log, articles
            WHERE log.path LIKE '%'||articles.slug AND
            log.method = 'GET'
            GROUP BY articles.title
            ORDER BY views {}
            LIMIT {}"""
    .format(order, limit))
rows = get_data(cur, query)
if rows is not None:
file = open('top_articles_report.txt', 'w')
return False
for row in rows:
file.write('"{}" - {} views \n'.format(row[0], row[1]))
file.close()
return True
