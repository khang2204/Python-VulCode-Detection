def sendIndexDocumentReq(ids):...
idStrList = ','
idStrList = idStrList.join(list(map(str, ids)))
sql = ('SELECT id, pagerank, date_updated FROM documents WHERE id IN (' +
    idStrList + ');')
print(ex)
return records
cursor.execute(sql)
return []
records = cursor.fetchall()
