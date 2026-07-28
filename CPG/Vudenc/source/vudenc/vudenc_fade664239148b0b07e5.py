def print_top_authors():...
"""docstring"""
print('What are the most popular article authors of all time?\n')
top_authors = '%s - %d views\n'
results = ''.join(top_authors % (name, views) for name, views in
    get_top_authors())
print(results)
