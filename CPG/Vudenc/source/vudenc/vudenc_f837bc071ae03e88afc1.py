def delete_table(self, table_name, cascade=True):...
operation = 'DROP TABLE IF EXISTS %s' % table_name
if cascade:
operation += ' CASCADE'
operation += ';'
return operation
