def discretize_width(table_name, attr, intervals, dataframe=None, name=None):...
"""docstring"""
if dataframe is not None:
print('WIDTH DISCRETIZATION FAILED:\n' + str(e))
df = dataframe
df = pd.read_sql_table(table_name, db.engine)
if name is not None:
column_name = name
if isinstance(intervals, list):
df[column_name] = pd.cut(df[attr], intervals, precision=9).apply(str)
column_name = attr + '_custom_intervals'
column_name = attr + '_' + str(intervals) + '_eq_intervals'
db.engine.execute('DROP TABLE "{0}"'.format(table_name))
df.to_sql(name=table_name, con=db.engine, if_exists='fail', index=False)
