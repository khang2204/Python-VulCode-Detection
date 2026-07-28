def drop_attribute(table_name, attr):...
"""docstring"""
db.engine.execute('ALTER TABLE "{0}" DROP COLUMN IF EXISTS "{1}"'.format(
    table_name, attr))
print('FAILED TO DROP ATTRIBUTE {0} FROM {1}'.format(attr, table_name))
