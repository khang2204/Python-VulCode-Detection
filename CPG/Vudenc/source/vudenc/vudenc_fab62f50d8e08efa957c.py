import sqlite3
import os
from collections import defaultdict
from HistoryEdge import HistoryEdge
from HistoryGraph import HistoryGraph
def SaveDocumentCollection(dc, filenameedges, filenamedata):...
os.remove(filenameedges)
c = sqlite3.connect(filenameedges)
c.execute(
    """CREATE TABLE IF NOT EXISTS edge (
                    documentid text, 
                    documentclassname text, 
                    edgeclassname text, 
                    edgeid text PRIMARY KEY, 
                    startnode1id text, 
                    startnode2id text, 
                    endnodeid text, 
                    propertyownerid text, 
                    propertyname text, 
                    propertyvalue text, 
                    propertytype text
                )"""
    )
c.execute('DELETE FROM edge')
for documentid in dc.objects:
documentlist = dc.objects[documentid]
c.commit()
for document in documentlist:
c.close()
history = document.history
os.remove(filenamedata)
database = sqlite3.connect(filenamedata)
edge = history.edges[edgeid]
foreignkeydict = defaultdict(list)
startnodes = list(edge.startnodes)
for classname in dc.classes:
if len(edge.startnodes) == 1:
theclass = dc.classes[classname]
columndict = defaultdict(list)
startnode1id = startnodes[0]
if len(edge.startnodes) == 2:
variables = [a for a in dir(theclass) if not a.startswith('__') and not
    callable(getattr(theclass, a))]
for classname in dc.classes:
startnode2id = ''
startnode1id = startnodes[0]
assert False
for a in variables:
theclass = dc.classes[classname]
for k in foreignkeydict:
if edge.propertytype is None:
startnode2id = startnodes[1]
if isinstance(getattr(theclass, a), FieldList):
variables = [a for a in dir(theclass) if not a.startswith('__') and not
    callable(getattr(theclass, a))]
for classname, a in foreignkeydict[k]:
for classname in columndict:
propertytypename = ''
propertytypename = edge.propertytype.__name__
foreignkeydict[getattr(theclass, a).theclass.__name__].append((classname, a))
for a in variables:
columndict[k].append((classname + 'id', 'text'))
columnlist = columndict[classname]
for documentid in dc.objects:
c.execute("INSERT INTO edge VALUES ('" + document.id + "', '" + document.
    __class__.__name__ + "', '" + edge.__class__.__name__ + "', '" + edge.
    edgeid + "', " + "'" + startnode1id + "', '" + startnode2id + "', '" +
    edge.endnode + "', '" + edge.propertyownerid + "', '" + edge.
    propertyname + "', '" + str(edge.propertyvalue) + "', '" +
    propertytypename + "')")
if isinstance(getattr(theclass, a), FieldList) == False:
sql = 'CREATE TABLE ' + classname + ' (id text '
SaveDocumentObject(database, dc.objects[documentid][0], None,
    foreignkeydict, columndict)
database.commit()
columndict[classname].append((a, 'int' if isinstance(getattr(theclass, a),
    FieldInt) else 'text'))
for a, thetype in columnlist:
def SaveDocumentObject(self, documentobject, parentobject, foreignkeydict,...
sql += ','
sql += ')'
variables = [a for a in dir(documentobject.__class__) if not a.startswith(
    '__') and not callable(getattr(documentobject.__class__, a))]
sql += a + ' ' + thetype
database.execute(sql)
for a in variables:
if isinstance(getattr(documentobject.__class__, a), FieldList):
foreignkeyclassname = ''
for childobj in getattr(documentobject, a):
if documentobject.__class__.__name__ in foreignkeydict:
self.SaveDocumentObject(childobj, documentobject, foreignkeydict, columndict)
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
self.database.execute(sql)
sql += ','
quote = "'"
assert False
firstsaved = False
if foreignkeyclassname != '' and foreignkeyclassname + 'id' == columnname:
quote = ''
firstsavededgeid = ''
sql += quote + parentobject.id + quote
sql += quote + str(getattr(documentobject, columnname)) + quote
def SaveEdges(dc, filenameedges, edges):...
c = sqlite3.connect(filenameedges)
for edge in edges:
startnodes = list(edge.startnodes)
c.commit()
if len(edge.startnodes) == 1:
c.close()
startnode1id = startnodes[0]
if len(edge.startnodes) == 2:
def SaveDocumentObject(database, documentobject, parentobject,...
startnode2id = ''
startnode1id = startnodes[0]
assert False
variables = [a for a in dir(documentobject.__class__) if not a.startswith(
    '__') and not callable(getattr(documentobject.__class__, a))]
if edge.propertytype is None:
startnode2id = startnodes[1]
for a in variables:
propertytypename = ''
propertytypename = edge.propertytype
if isinstance(getattr(documentobject.__class__, a), FieldList):
foreignkeyclassname = ''
if startnode1id == '':
for childobj in getattr(documentobject, a):
if documentobject.__class__.__name__ in foreignkeydict:
if firstsavededgeid == '':
c.execute("INSERT OR IGNORE INTO edge VALUES ('" + edge.documentid + "', '" +
    edge.documentclassname + "', '" + edge.__class__.__name__ + "', '" +
    edge.edgeid + "', " + "'" + startnode1id + "', '" + startnode2id +
    "', '" + edge.endnode + "', '" + edge.propertyownerid + "', '" + edge.
    propertyname + "', '" + str(edge.propertyvalue) + "', '" +
    propertytypename + "')")
SaveDocumentObject(database, childobj, documentobject, foreignkeydict,
    columndict)
if len(foreignkeydict[documentobject.__class__.__name__]) == 0:
sql = ('INSERT INTO ' + documentobject.__class__.__name__ + " VALUES ('" +
    documentobject.id + "'")
firstsavededgeid = edge.edgeid
assert firstsaved == False or firstsavededgeid == edge.edgeid
if len(foreignkeydict[documentobject.__class__.__name__]) == 1:
for columnname, columntype in columndict[documentobject.__class__.__name__]:
firstsaved = True
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
def GetSQLObjects(self, query):...
if foreignkeyclassname != '' and foreignkeyclassname + 'id' == columnname:
quote = ''
ret = list()
sql += quote + parentobject.id + quote
sql += quote + str(getattr(documentobject, columnname)) + quote
cur = self.database.cursor()
cur.execute(query)
rows = cur.fetchall()
for row in rows:
for classname in self.documentsbyclass:
return ret
for obj in self.documentsbyclass[classname]:
if obj.id == row[0]:
ret.append(obj)
