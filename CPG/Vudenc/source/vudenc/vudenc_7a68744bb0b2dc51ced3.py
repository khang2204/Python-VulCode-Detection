def restore_original(table_name):...
"""docstring"""
original = 'og' + table_name[2:]
print('FAILED TO RESTORE ORIGINAL')
db.engine.execute('DROP TABLE "{0}"'.format(table_name))
db.engine.execute('CREATE TABLE "{0}" AS SELECT * FROM "{1}"'.format(
    table_name, original))
