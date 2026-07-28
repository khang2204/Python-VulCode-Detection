def GetSQLObjects(database, documentcollection, query):...
ret = list()
cur = database.cursor()
cur.execute(query)
rows = cur.fetchall()
for row in rows:
for classname in documentcollection.objects:
return ret
for obj in documentcollection.objects[classname]:
if obj.id == row[0]:
ret.append(obj)
