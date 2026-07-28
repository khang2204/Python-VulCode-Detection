def update_where(self, table, info, where):...
"""docstring"""
self.cursor.execute('UPDATE {0} SET {1} WHERE {2}'.format(table, info, where))
print('Erro: {}'.format(error))
self.__connection.commit()
return self.cursor
