def get_switched_path(switch1, switch2, rtype='NGTREE', verbose=True):...
"""docstring"""
rtypes = 'CSV', 'TREE', 'JSON', 'YAML', 'NGTREE'
if rtype in rtypes:
logger.info('Query: Finding Switched Paths (%s --> %s) for %s', switch1,
    switch2, nglib.user)
return
pathList = []
ngtree = nglib.ngtree.get_ngtree('Switched Paths', tree_type='L2-PATH')
ngtree['Name'] = switch1 + ' -> ' + switch2
dist = dict()
swp = nglib.py2neo_ses.cypher.execute('MATCH (ss:Switch), (ds:Switch), ' +
    'sp = allShortestPaths((ss)-[:NEI*0..9]-(ds)) ' +
    'WHERE ss.name =~ {switch1} AND ds.name =~ {switch2}' +
    'UNWIND nodes(sp) as s1 UNWIND nodes(sp) as s2 ' +
    'MATCH (s1)<-[nei:NEI]-(s2), plen = shortestPath((ss)-[:NEI*0..9]-(s1)) ' +
    'RETURN DISTINCT s1.name AS csw, s2.name AS psw, ' +
    'nei.pPort AS pport, nei.cPort as cport, nei.native AS native, ' +
    'nei.cPc as cPc, nei.pPc AS pPc, nei.vlans AS vlans, nei.rvlans as rvlans, '
     + 'nei._rvlans AS p_rvlans, ' +
    'LENGTH(plen) as distance ORDER BY distance, s1.name, s2.name', {
    'switch1': switch1, 'switch2': switch2})
last = 0
for rec in swp:
swptree = nglib.ngtree.get_ngtree('Link', tree_type='L2-HOP')
if pathList:
if rec.distance == 0:
ngtree['Links'] = len(pathList)
if verbose:
swptree['distance'] = rec.distance + 1
if last:
ngtree['Distance'] = max([s['distance'] for s in pathList])
print('No results found for path between {:} and {:}'.format(switch1, switch2))
last = 1
if rec.distance == last:
swptree['distance'] = rec.distance
if rtype == 'CSV':
swptree['Name'] = ('#' + str(swptree['distance']) + ' ' + rec.psw + '(' +
    rec.pport + ') <-> ' + rec.csw + '(' + rec.cport + ')')
last += 1
if rec.distance == last - 1:
nglib.query.print_dict_csv(pathList)
ngtree = nglib.query.exp_ngtree(ngtree, rtype)
nglib.ngtree.add_child_ngtree(ngtree, swptree)
swptree['distance'] = rec.distance + 1
swptree['distance'] = rec.distance + 1
swptree['distance'] = rec.distance
return ngtree
swptree['Child Switch'] = rec.csw
last = 0
swptree['Child Port'] = rec.cport
swptree['Parent Switch'] = rec.psw
swptree['Parent Port'] = rec.pport
if rec.cPc:
swptree['Child Channel'] = rec.cPc
if rec.rvlans:
swptree['Parent Channel'] = rec.pPc
swptree['Link VLANs'] = rec.vlans
pathList.append(swptree)
swptree['Link rVLANs'] = rec.rvlans
swptree['_rvlans'] = rec.p_rvlans
swptree['Native VLAN'] = rec.native
