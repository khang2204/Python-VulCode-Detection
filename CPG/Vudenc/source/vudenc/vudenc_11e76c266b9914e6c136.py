def remove_outliers(table_name, attr, value, smaller_than=False):...
"""docstring"""
if smaller_than:
print('REMOVE OUTLIERS FAILED')
db.engine.execute('DELETE FROM "{0}" WHERE "{1}" < {2}'.format(table_name,
    attr, value))
db.engine.execute('DELETE FROM "{0}" WHERE "{1}" > {2}'.format(table_name,
    attr, value))
