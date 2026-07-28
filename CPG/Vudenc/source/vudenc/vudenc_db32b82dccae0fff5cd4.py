def one_hot_encode(table_name, attr):...
"""docstring"""
dataframe = pd.read_sql_table(table_name, db.engine)
print('ONE-HOT ENCODING FAILED')
one_hot = pd.get_dummies(dataframe[attr])
print('OH', one_hot)
dataframe = dataframe.join(one_hot)
print('DF', dataframe)
db.engine.execute('DROP TABLE "{0}"'.format(table_name))
dataframe.to_sql(name=table_name, con=db.engine, if_exists='fail', index=False)
