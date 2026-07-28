from app import database as db
import pandas as pd
import re
import numpy as np
def rename_attribute(table_name, column, new_name):...
db.engine.execute('ALTER TABLE {0} RENAME COLUMN "{1}" TO "{2}"'.format(
    table_name, column, new_name))
print('RENAMING FAILED: ' + str(e))
def delete_attribute(table_name, column):...
db.engine.execute('ALTER TABLE {0} DROP COLUMN "{1}"'.format(table_name,
    column))
print('DELETING FAILED')
def restore_original(table_name):...
"""docstring"""
original = 'og' + table_name[2:]
print('FAILED TO RESTORE ORIGINAL')
def change_attribute_type(table_name, table_col, new_type):...
db.engine.execute('DROP TABLE "{0}"'.format(table_name))
"""docstring"""
db.engine.execute('CREATE TABLE "{0}" AS SELECT * FROM "{1}"'.format(
    table_name, original))
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
def drop_attribute(table_name, attr):...
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE TIMESTAMP WITH TIME ZONE'.
    format(table_name, table_col))
db.engine.execute(
    'ALTER TABLE {0} ALTER COLUMN "{1}" TYPE TIMESTAMP WITH TIME ZONE USING to_timestamp("{1}", \'DD/MM/YYYY HH24:MI:SS\')'
    .format(table_name, table_col))
"""docstring"""
db.engine.execute('ALTER TABLE "{0}" DROP COLUMN IF EXISTS "{1}"'.format(
    table_name, attr))
print('FAILED TO DROP ATTRIBUTE {0} FROM {1}'.format(attr, table_name))
def one_hot_encode(table_name, attr):...
"""docstring"""
dataframe = pd.read_sql_table(table_name, db.engine)
print('ONE-HOT ENCODING FAILED')
def fill_null_with(table_name, attr, value, text_type):...
one_hot = pd.get_dummies(dataframe[attr])
"""docstring"""
print('OH', one_hot)
if text_type:
print('FILL NULL FAILED WITH FOLLOWING MESSAGE:\n' + str(e))
def fill_null_with_average(table_name, attr):...
dataframe = dataframe.join(one_hot)
db.engine.execute(
    'UPDATE "{0}" SET "{1}" = \'{2}\' WHERE ("{1}" = \'\') IS NOT FALSE'.
    format(table_name, attr, value))
db.engine.execute('UPDATE "{0}" SET "{1}" = {2} WHERE "{1}" IS NULL'.format
    (table_name, attr, value))
"""docstring"""
print('DF', dataframe)
dataframe = pd.read_sql_table(table_name, db.engine, columns=[attr])
print('FILL AVERAGE FAILED')
def fill_null_with_median(table_name, attr):...
db.engine.execute('DROP TABLE "{0}"'.format(table_name))
average = dataframe[attr].mean()
"""docstring"""
dataframe.to_sql(name=table_name, con=db.engine, if_exists='fail', index=False)
db.engine.execute('UPDATE "{0}" SET "{1}" = {2} WHERE "{1}" IS NULL'.format
    (table_name, attr, average))
dataframe = pd.read_sql_table(table_name, db.engine, columns=[attr])
print('FILL MEAN FAILED')
def find_replace(table_name, attr, find, replace):...
median = dataframe[attr].median()
db.engine.execute('UPDATE "{0}" SET "{1}" = \'{2}\' WHERE "{1}" = \'{3}\' '
    .format(table_name, attr, replace, find))
print('FIND-REPLACE FAILED')
def substring_find_replace(table_name, attr, find, replace, full=False):...
db.engine.execute('UPDATE "{0}" SET "{1}" = {2} WHERE "{1}" IS NULL'.format
    (table_name, attr, median))
if full:
print('FIND-REPLACE FAILED\n' + str(e))
def regex_find_replace(table_name, attr, regex, replace):...
db.engine.execute(
    'UPDATE "{0}" SET "{1}" = \'{2}\' WHERE "{1}" LIKE \'%%{3}%%\' '.format
    (table_name, attr, replace, find))
db.engine.execute('UPDATE "{0}" SET "{1}" = REPLACE("{1}", \'{2}\', \'{3}\')'
    .format(table_name, attr, find, replace))
is_valid = True
print('REGEX FIND-REPLACE FAILED:\n' + str(e))
def normalize_attribute(table_name, attr):...
re.compile(regex)
is_valid = False
if is_valid:
"""docstring"""
db.engine.execute(
    'UPDATE "{0}" SET "{1}" = REGEXP_REPLACE("{1}", \'{2}\', \'{3}\')'.
    format(table_name, attr, regex, replace))
df = pd.read_sql_table(table_name, db.engine)
print('NORMALIZATION FAILED')
def remove_outliers(table_name, attr, value, smaller_than=False):...
df[attr] = (df[attr] - df[attr].mean()) / df[attr].std(ddof=0)
"""docstring"""
db.engine.execute('DROP TABLE "{0}"'.format(table_name))
if smaller_than:
print('REMOVE OUTLIERS FAILED')
def delete_rows(table_name, condition):...
df.to_sql(name=table_name, con=db.engine, if_exists='fail', index=False)
db.engine.execute('DELETE FROM "{0}" WHERE "{1}" < {2}'.format(table_name,
    attr, value))
db.engine.execute('DELETE FROM "{0}" WHERE "{1}" > {2}'.format(table_name,
    attr, value))
db.engine.execute('DELETE FROM "{0}" WHERE {1}'.format(table_name, condition))
def discretize_width(table_name, attr, intervals, dataframe=None, name=None):...
"""docstring"""
if dataframe is not None:
print('WIDTH DISCRETIZATION FAILED:\n' + str(e))
def discretize_eq_freq(table_name, attr, intervals):...
df = dataframe
df = pd.read_sql_table(table_name, db.engine)
"""docstring"""
if name is not None:
df = pd.read_sql_table(table_name, db.engine)
print('EQUAL FREQUENCY DISCRETIZATION FAILED:\n' + str(e))
column_name = name
if isinstance(intervals, list):
attr_length = len(df[attr])
df[column_name] = pd.cut(df[attr], intervals, precision=9).apply(str)
column_name = attr + '_custom_intervals'
column_name = attr + '_' + str(intervals) + '_eq_intervals'
elements_per_interval = attr_length // intervals
db.engine.execute('DROP TABLE "{0}"'.format(table_name))
sorted_data = list(df[attr].sort_values())
df.to_sql(name=table_name, con=db.engine, if_exists='fail', index=False)
selector = 0
edge_list = []
while selector < attr_length:
if edge_list[-1] != sorted_data[-1] and len(edge_list) == intervals + 1:
edge_list.append(sorted_data[selector])
edge_list[-1] = sorted_data[-1]
if edge_list[-1] != sorted_data[-1] and len(edge_list) != intervals + 1:
selector += elements_per_interval
edge_list[0] = edge_list[0] - edge_list[0] * 0.001
edge_list.append(sorted_data[-1])
edge_list[-1] = edge_list[-1] + edge_list[-1] * 0.001
column_name = attr + '_' + str(intervals) + '_eq_freq_intervals'
discretize_width(table_name, attr, edge_list, df, column_name)
