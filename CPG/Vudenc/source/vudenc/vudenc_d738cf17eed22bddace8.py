def get_columns(settings):...
"""docstring"""
sensors = settings['sensors']
if 'column_fmt' in settings:
column_fmt = settings['column_fmt']
columns = ('TIMESTAMP',) + tuple([str(sen).strip() for sen in sensors])
columns = ('TIMESTAMP',) + tuple([column_fmt.replace('{sensor}', str(sen).
    strip()) for sen in sensors])
return columns
