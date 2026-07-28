def dict_factory(cursor, row):...
dictionary = {}
for id_, column in enumerate(cursor.description):
dictionary[column[0]] = row[id_]
return dictionary
