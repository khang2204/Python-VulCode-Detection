def main():...
"""docstring"""
conn = setup_connection('news')
if conn is not None:
cur = conn.cursor()
if get_top_articles(cur, 'DESC', 3):
print('Successful creating top articles report.')
print('Error creating top articles report.')
if get_top_authors(cur, 'DESC'):
print('Successful creating top authors report.')
print('Error creating top authors report.')
if get_error_days(cur, 1):
print('Successful creating daily error percentage report.')
print('Error creating daily error percentage report.')
conn.close()
