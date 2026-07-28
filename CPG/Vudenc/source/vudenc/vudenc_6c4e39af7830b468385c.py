def get_top_authors(cur, order):...
"""docstring"""
query = (
    """SELECT authors.name, COUNT(*) as views
            FROM authors, articles, log
            WHERE authors.id = articles.author AND
            log.path LIKE '%'||articles.slug AND
            log.method = 'GET'
            GROUP BY authors.name
            ORDER BY views {}"""
    .format(order))
rows = get_data(cur, query)
if rows is not None:
file = open('top_authors_report.txt', 'w')
return False
for row in rows:
file.write('{} - {} views \n'.format(row[0], row[1]))
file.close()
return True
