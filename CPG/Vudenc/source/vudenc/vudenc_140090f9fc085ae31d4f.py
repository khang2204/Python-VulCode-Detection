def change_attribute_type(table_name, table_col, new_type):...
"""docstring"""
current_type = db.engine.execute(
    "SELECT data_type from information_schema.columns where table_name = '{0}' and column_name = '{1}';"
    .format(table_name, table_col)).fetchall()[0][0]
if new_type == 'INTEGER':
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE BIGINT USING "{1}"::bigint'.
    format(table_name, table_col))
if new_type == 'DOUBLE':
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE DOUBLE PRECISION USING "{1}"::double precision'
    .format(table_name, table_col))
if new_type == 'TEXT':
if current_type == 'date':
if new_type == 'DATE':
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE TEXT USING to_char("{1}", \'DD/MM/YYYY\')'
    .format(table_name, table_col))
if current_type == 'timestamp with time zone':
if current_type == 'timestamp with time zone':
if new_type == 'TIMESTAMP':
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE TEXT USING to_char("{1}", \'DD/MM/YYYY HH24:MI:SS\')'
    .format(table_name, table_col))
db.engine.execute('ALTER TABLE {0} ALTER COLUMN "{1}" TYPE TEXT'.format(
    table_name, table_col))
db.engine.execute('ALTER TABLE {0} ALTER COLUMN "{1}" TYPE DATE'.format(
    table_name, table_col))
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE DATE USING to_date("{1}", \'DD/MM/YYYY\')'
    .format(table_name, table_col))
if current_type == 'date':
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE TIMESTAMP WITH TIME ZONE'.
    format(table_name, table_col))
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE TIMESTAMP WITH TIME ZONE USING to_timestamp("{1}", \'DD/MM/YYYY HH24:MI:SS\')'
    .format(table_name, table_col))
