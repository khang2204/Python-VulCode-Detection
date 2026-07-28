def select(self, table):...
"""docstring"""
aux_dict = dict()
self.cursor.execute('SELECT * FROM {0}'.format(table))
json_data = {}
for user in self.cursor:
json_data[str(user[3])] = {}
return json.dumps(json_data)
json_data[str(user[3])]['nome'] = user[0]
json_data[str(user[3])]['sobrenome'] = user[1]
json_data[str(user[3])]['endereco'] = user[2]
