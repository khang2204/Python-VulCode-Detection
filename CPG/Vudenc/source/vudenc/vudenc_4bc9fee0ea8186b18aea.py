def convert_search(search):...
"""docstring"""
if not search:
search = ''
search = search.replace('*', '%').replace(' ', '%')
if search and search.startswith('^'):
search = search.replace('^', '')
if search and search.endswith('$'):
search += '%'
search = search.replace('$', '')
search = '%' + search + '%'
return search
search = '%' + search
