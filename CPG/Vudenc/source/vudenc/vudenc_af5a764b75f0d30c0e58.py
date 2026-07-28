def normalize_attribute(table_name, attr):...
"""docstring"""
df = pd.read_sql_table(table_name, db.engine)
print('NORMALIZATION FAILED')
df[attr] = (df[attr] - df[attr].mean()) / df[attr].std(ddof=0)
db.engine.execute('DROP TABLE "{0}"'.format(table_name))
df.to_sql(name=table_name, con=db.engine, if_exists='fail', index=False)
