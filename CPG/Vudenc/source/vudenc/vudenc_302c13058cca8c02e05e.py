def get_routed_path(net1, net2, rtype='NGTREE', vrf='default', verbose=True,...
"""docstring"""
rtypes = 'CSV', 'TREE', 'JSON', 'YAML', 'NGTREE'
if rtype in rtypes:
logger.info('Query: Finding Routed Paths (%s --> %s) for %s', net1, net2,
    nglib.user)
return
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', net1):
n1tree = nglib.query.net.get_net(net1, rtype='NGTREE')
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', net2):
net1 = n1tree['_child001']['Name']
n2tree = nglib.query.net.get_net(net2, rtype='NGTREE')
ngtree = nglib.ngtree.get_ngtree('Path', tree_type='L3-PATH')
if n2tree:
ngtree['Path'] = net1 + ' -> ' + net2
net2 = n2tree['_child001']['Name']
ngtree['Name'] = ngtree['Path']
pathList = []
pathRec = []
rtrp = nglib.py2neo_ses.cypher.execute(
    'MATCH (sn:Network), (dn:Network), rp = allShortestPaths ' +
    '((sn)-[:ROUTED|ROUTED_BY|ROUTED_STANDBY*0..12]-(dn)) ' +
    'WHERE ALL(v IN rels(rp) WHERE v.vrf = {vrf}) ' +
    'AND sn.cidr =~ {net1} AND dn.cidr =~ {net2}' +
    'UNWIND nodes(rp) as r1 UNWIND nodes(rp) as r2 ' +
    'MATCH (r1)<-[l1:ROUTED]-(n:Network {vrf:{vrf}})-[l2:ROUTED]->(r2) ' +
    'OPTIONAL MATCH (n)-[:L3toL2]->(v:VLAN) ' +
    'RETURN DISTINCT r1.name AS r1name, l1.gateway AS r1ip, ' +
    'r2.name AS r2name, l2.gateway as r2ip, v.vid AS vid, ' +
    'LENGTH(shortestPath((sn)<-[:ROUTED|ROUTED_BY|ROUTED_STANDBY*0..12]->(r1))) '
     + 'AS distance ORDER BY distance', {'net1': net1, 'net2': net2, 'vrf':
    vrf})
allpaths = dict()
for rec in rtrp:
p = rec['r1name'], rec['r2name']
for en in allpaths:
allpaths[p] = rec['distance']
if allpaths[en] < allpaths[tuple(reversed(en))]:
pathRec = sorted(pathRec, key=lambda tup: (tup[2], tup[0], tup[1]))
r1, r2 = en
for path in pathRec:
distance = allpaths[en]
for rec in rtrp:
if pathList:
pathRec.append((r1, r2, distance))
if path[0] == rec['r1name'] and path[1] == rec['r2name']:
ngtree['Hops'] = len(pathList)
if verbose:
rtree = nglib.ngtree.get_ngtree('Hop', tree_type='L3-HOP')
ngtree['Max Hops'] = max([s['distance'] for s in pathList])
print('No results found for path between {:} and {:}'.format(net1, net2),
    file=sys.stderr)
rtree['From Router'] = rec['r1name']
ngtree['VRF'] = vrf
rtree['From IP'] = rec['r1ip']
if rtype == 'CSV':
rtree['To Router'] = rec['r2name']
nglib.query.print_dict_csv(pathList)
ngtree = nglib.query.exp_ngtree(ngtree, rtype)
rtree['To IP'] = rec['r2ip']
return ngtree
rtree['VLAN'] = rec['vid']
distance = rec['distance']
if distance != 1:
distance = int((distance - 1) / 2) + 1
rtree['distance'] = distance
rtree['Name'] = '#{:} {:}({:}) -> {:}({:})'.format(distance, rec['r1name'],
    rec['r1ip'], rec['r2name'], rec['r2ip'])
if l2path:
spath = get_switched_path(rec['r1name'], rec['r2name'], verbose=False)
nglib.ngtree.add_child_ngtree(ngtree, rtree)
for sp in spath:
pathList.append(rtree)
if '_child' in sp and '_rvlans' in spath[sp]:
vrgx = '[^0-9]*' + rec['vid'] + '[^0-9]*'
if re.search(vrgx, spath[sp]['_rvlans']):
nglib.ngtree.add_child_ngtree(rtree, spath[sp])
