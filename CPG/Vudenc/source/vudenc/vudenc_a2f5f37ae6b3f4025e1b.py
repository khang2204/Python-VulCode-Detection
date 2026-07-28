def print_top_articles(list_count):...
"""docstring"""
print('What are the most popular %d articles of all time?\n' % list_count)
top_articles = '"%s" - %d views\n'
results = ''.join(top_articles % (title, views) for title, views in
    get_top_articles(list_count))
print(results)
