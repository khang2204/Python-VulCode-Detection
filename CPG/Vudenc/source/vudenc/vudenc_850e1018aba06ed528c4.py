def delete_where(self, table, where):...
"""docstring"""
self.cursor.execute('DELETE FROM {0} WHERE {1}'.format(table, where))
print('Erro: {}'.format(error))
self.__connection.commit()
return self.cursor
