def insert(self, table, content):...
"""docstring"""
nome = content['nome']
sobrenome = content['sobrenome']
endereco = content['endereco']
add_user = 'INSERT INTO users (nome, sobrenome, endereco) VALUES (%s,%s,%s)'
data_user = nome, sobrenome, endereco
self.cursor.execute(add_user, data_user)
print('Error: {}'.format(error))
self.__connection.commit()
self.cursor.lastrowid
