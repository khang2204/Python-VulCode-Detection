def _addColumn(self, column, init_data):...
"""docstring"""
command = 'ALTER TABLE ' + TABLE_NAME + ' ADD COLUMN ' + str(column
    ) + ' ' + getSQLiteType(init_data)
self._run_command(command)
print('Column ' + str(column) + ' already exists!')
