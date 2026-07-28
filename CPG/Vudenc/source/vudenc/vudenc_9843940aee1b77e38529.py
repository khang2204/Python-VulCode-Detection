def SaveEdges(dc, filenameedges, edges):...
c = sqlite3.connect(filenameedges)
for edge in edges:
startnodes = list(edge.startnodes)
c.commit()
if len(edge.startnodes) == 1:
c.close()
startnode1id = startnodes[0]
if len(edge.startnodes) == 2:
startnode2id = ''
startnode1id = startnodes[0]
assert False
if edge.propertytype is None:
startnode2id = startnodes[1]
propertytypename = ''
propertytypename = edge.propertytype
if startnode1id == '':
if firstsavededgeid == '':
c.execute("INSERT OR IGNORE INTO edge VALUES ('" + edge.documentid + "', '" +
    edge.documentclassname + "', '" + edge.__class__.__name__ + "', '" +
    edge.edgeid + "', " + "'" + startnode1id + "', '" + startnode2id +
    "', '" + edge.endnode + "', '" + edge.propertyownerid + "', '" + edge.
    propertyname + "', '" + str(edge.propertyvalue) + "', '" +
    propertytypename + "')")
firstsavededgeid = edge.edgeid
assert firstsaved == False or firstsavededgeid == edge.edgeid
firstsaved = True
