"""
Network Path Algorithms Between Switches and Routers

"""
import re
import sys
import logging
import subprocess
import nglib
import nglib.query.nNode
import nglib.netdb.ip
logger = logging.getLogger(__name__)
def get_full_path(src, dst, rtype='NGTREE'):...
"""docstring"""
rtypes = 'CSV', 'TREE', 'JSON', 'YAML', 'NGTREE'
if rtype in rtypes:
logger.info('Query: Finding Full Path (%s --> %s) for %s', src, dst, nglib.user
    )
def get_full_routed_path(src, dst, rtype='NGTREE', l2path=False):...
net1, net2 = src, dst
"""docstring"""
n1tree, n2tree = None, None
rtypes = 'CSV', 'TREE', 'JSON', 'YAML', 'NGTREE'
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', net1):
if rtype in rtypes:
n1tree = nglib.query.net.get_net(net1, rtype='NGTREE')
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', net2):
srct, dstt, ngtree = None, None, None
def get_switched_path(switch1, switch2, rtype='NGTREE', verbose=True):...
if n1tree:
n2tree = nglib.query.net.get_net(net2, rtype='NGTREE')
srctree, dsttree, srcswp, dstswp = None, None, None, None
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', src):
"""docstring"""
net1 = n1tree['_child001']['Name']
if n2tree:
if nglib.use_netdb:
srct = nglib.query.net.get_net(src, rtype='NGTREE')
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', dst):
rtypes = 'CSV', 'TREE', 'JSON', 'YAML', 'NGTREE'
net2 = n2tree['_child001']['Name']
srctree = nglib.netdb.ip.get_netdb_ip(src)
if srctree:
dstt = nglib.query.net.get_net(dst, rtype='NGTREE')
if srct['_child001']['VRF'] == dstt['_child001']['VRF']:
if rtype in rtypes:
dsttree = nglib.netdb.ip.get_netdb_ip(dst)
router = n1tree['_child001']['Router']
if dsttree:
ngtree = get_routed_path(src, dst, verbose=False)
secpath = get_fw_path(src, dst, rtype='NGTREE')
logger.info('Query: Finding Switched Paths (%s --> %s) for %s', switch1,
    switch2, nglib.user)
return
if 'StandbyRouter' in n1tree['_child001']:
router = n2tree['_child001']['Router']
switching = True
return ngtree
ngtree = nglib.ngtree.get_ngtree(secpath['Name'], tree_type='L4-PATH')
pathList = []
router = router + '|' + n1tree['_child001']['StandbyRouter']
srcswp = get_switched_path(srctree['Switch'], router, verbose=False)
if 'StandbyRouter' in n2tree['_child001']:
if srctree and dsttree:
first = True
ngtree = nglib.ngtree.get_ngtree('Switched Paths', tree_type='L2-PATH')
router = router + '|' + n2tree['_child001']['StandbyRouter']
dstswp = get_switched_path(router, dsttree['Switch'], verbose=False)
if srctree['Switch'] == dsttree['Switch'] and srctree['VLAN'] == dsttree['VLAN'
ngtree = nglib.ngtree.get_ngtree('L2-L4', tree_type='PATHs')
last = None
ngtree['Name'] = switch1 + ' -> ' + switch2
switching = False
if n1tree['_child001']['Name'] != n2tree['_child001']['Name']:
for key in sorted(secpath.keys()):
dist = dict()
ngtree['L3 Path'] = net1 + ' -> ' + net2
if srctree and dsttree:
if '_child' in key:
if last:
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
ngtree['Lx Path'] = src + ' -> ' + dst
ngtree['L2 Path'] = srctree['Switch'] + ' (' + srctree['SwitchPort'
    ] + ') -> ' + dsttree['Switch'] + ' (' + dsttree['SwitchPort'] + ')'
n1tree['_type'] = 'SRC'
if re.search('(Network|FW)', secpath[key]['Name']):
rtree = get_routed_path(secpath[last]['gateway'], dst, vrf=dstt['_child001'
    ]['VRF'], l2path=l2path)
last = 0
n1tree['Name'] = src
if first:
if rtree:
for rec in swp:
nglib.ngtree.add_child_ngtree(ngtree, n1tree)
rtree = get_routed_path(src, secpath[key]['gateway'], vrf=srct['_child001']
    ['VRF'], l2path=l2path)
nglib.ngtree.add_child_ngtree(ngtree, secpath[key])
nglib.ngtree.add_child_ngtree(ngtree, rtree)
swptree = nglib.ngtree.get_ngtree('Link', tree_type='L2-HOP')
if pathList:
if not switching and '_child002' in n2tree:
if rtree:
last = key
if rec.distance == 0:
ngtree['Links'] = len(pathList)
if verbose:
nglib.ngtree.add_child_ngtree(n1tree, n2tree['_child002'])
if switching and srcswp:
nglib.ngtree.add_child_ngtree(ngtree, rtree)
first = False
swptree['distance'] = rec.distance + 1
if last:
ngtree['Distance'] = max([s['distance'] for s in pathList])
print('No results found for path between {:} and {:}'.format(switch1, switch2))
n1tree['_type'] = 'L2PATH'
nglib.ngtree.add_child_ngtree(ngtree, srcswp)
rtree = get_full_routed_path(src, dst, rtype='NGTREE', l2path=True)
last = 1
if rec.distance == last:
swptree['distance'] = rec.distance
if rtype == 'CSV':
n1tree['Name'] = src + ' -> ' + dst
if rtree and 'PATH' in rtree['_type']:
swptree['Name'] = ('#' + str(swptree['distance']) + ' ' + rec.psw + '(' +
    rec.pport + ') <-> ' + rec.csw + '(' + rec.cport + ')')
last += 1
if rec.distance == last - 1:
nglib.query.print_dict_csv(pathList)
ngtree = nglib.query.exp_ngtree(ngtree, rtype)
if rtree['_type'] == 'L4-PATH':
if switching and dstswp:
nglib.ngtree.add_child_ngtree(ngtree, swptree)
swptree['distance'] = rec.distance + 1
swptree['distance'] = rec.distance + 1
swptree['distance'] = rec.distance
return ngtree
ngtree['L4 Path'] = rtree['Name']
ngtree['L4 Path'] = 'VRF:' + n1tree['_child001']['VRF']
nglib.ngtree.add_child_ngtree(ngtree, dstswp)
if switching:
swptree['Child Switch'] = rec.csw
last = 0
nglib.ngtree.add_child_ngtree(ngtree, rtree)
n2tree['_type'] = 'DST'
ngtree = nglib.query.exp_ngtree(ngtree, rtype)
swptree['Child Port'] = rec.cport
n2tree['Name'] = dst
return ngtree
swptree['Parent Switch'] = rec.psw
nglib.ngtree.add_child_ngtree(ngtree, n2tree)
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
