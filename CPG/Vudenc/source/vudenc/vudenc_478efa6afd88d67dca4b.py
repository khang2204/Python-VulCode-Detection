def SaveDocumentObject(database, documentobject, parentobject,...
variables = [a for a in dir(documentobject.__class__) if not a.startswith(
    '__') and not callable(getattr(documentobject.__class__, a))]
for a in variables:
if isinstance(getattr(documentobject.__class__, a), FieldList):
foreignkeyclassname = ''
for childobj in getattr(documentobject, a):
if documentobject.__class__.__name__ in foreignkeydict:
SaveDocumentObject(database, childobj, documentobject, foreignkeydict,
    columndict)
if len(foreignkeydict[documentobject.__class__.__name__]) == 0:
sql = ('INSERT INTO ' + documentobject.__class__.__name__ + " VALUES ('" +
    documentobject.id + "'")
if len(foreignkeydict[documentobject.__class__.__name__]) == 1:
for columnname, columntype in columndict[documentobject.__class__.__name__]:
foreignkeyclassname, a = foreignkeydict[documentobject.__class__.__name__][0]
assert False
if columntype == 'int':
sql += ')'
quote = ''
if columntype == 'text':
database.execute(sql)
sql += ','
quote = "'"
assert False
if foreignkeyclassname != '' and foreignkeyclassname + 'id' == columnname:
quote = ''
sql += quote + parentobject.id + quote
sql += quote + str(getattr(documentobject, columnname)) + quote
