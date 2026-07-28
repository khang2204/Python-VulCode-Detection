def fill_null_with(table_name, attr, value, text_type):...
"""docstring"""
if text_type:
print('FILL NULL FAILED WITH FOLLOWING MESSAGE:\n' + str(e))
db.engine.execute(
    'UPDATE "{0}" SET "{1}" = \'{2}\' WHERE ("{1}" = \'\') IS NOT FALSE'.
    format(table_name, attr, value))
db.engine.execute('UPDATE "{0}" SET "{1}" = {2} WHERE "{1}" IS NULL'.format
    (table_name, attr, value))
