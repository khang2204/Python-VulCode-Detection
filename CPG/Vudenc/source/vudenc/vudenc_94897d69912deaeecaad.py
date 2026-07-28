def LoadDocumentCollection(dc, filenameedges, filenamedata):...
dc.objects = defaultdict(list)
dc.historyedgeclasses = dict()
for theclass in HistoryEdge.__subclasses__():
dc.historyedgeclasses[theclass.__name__] = theclass
c = sqlite3.connect(filenameedges)
cur = c.cursor()
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
c.commit()
cur.execute(
    'SELECT documentid, documentclassname, edgeclassname, edgeid, startnode1id, startnode2id, endnodeid, propertyownerid, propertyname, propertyvalue, propertytype FROM edge'
    )
historygraphdict = defaultdict(HistoryGraph)
documentclassnamedict = dict()
rows = cur.fetchall()
for row in rows:
documentid = row[0]
nulledges = list()
documentclassname = row[1]
for documentid in historygraphdict:
edgeclassname = row[2]
doc = dc.classes[documentclassnamedict[documentid]](documentid)
SaveEdges(dc, filenameedges, nulledges)
edgeid = row[3]
nulledges.extend(history.MergeDanglingBranches())
return sqlite3.connect(filenamedata)
startnode1id = row[4]
history.Replay(doc)
startnode2id = row[5]
dc.AddDocumentObject(doc)
endnodeid = row[6]
propertyownerid = row[7]
propertyname = row[8]
propertyvaluestr = row[9]
propertytypestr = row[10]
if documentid in historygraphdict:
historygraph = historygraphdict[documentid]
historygraph = HistoryGraph()
if propertytypestr == 'FieldInt':
historygraphdict[documentid] = historygraph
propertyvalue = int(propertyvaluestr)
if propertytypestr == 'FieldText':
documentclassnamedict[documentid] = documentclassname
documentclassnamedict[documentid] = documentclassname
propertyvalue = str(propertyvaluestr)
if propertytypestr == '' and edgeclassname == 'HistoryEdgeNull':
if startnode2id == '':
propertyvalue = ''
propertyvalue = propertyvaluestr
startnodes = {startnode1id}
startnodes = {startnode1id, startnode2id}
edge = dc.historyedgeclasses[edgeclassname](edgeid, startnodes, endnodeid,
    propertyownerid, propertyname, propertyvalue, propertytypestr,
    documentid, documentclassname)
history = historygraphdict[documentid]
history.AddEdge(edge)
