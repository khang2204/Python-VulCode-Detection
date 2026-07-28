def fill_null_with_median(table_name, attr):...
"""docstring"""
dataframe = pd.read_sql_table(table_name, db.engine, columns=[attr])
print('FILL MEAN FAILED')
median = dataframe[attr].median()
db.engine.execute('UPDATE "{0}" SET "{1}" = {2} WHERE "{1}" IS NULL'.format
    (table_name, attr, median))
