def get_full_path(src, dst, rtype='NGTREE'):...
"""docstring"""
rtypes = 'CSV', 'TREE', 'JSON', 'YAML', 'NGTREE'
if rtype in rtypes:
logger.info('Query: Finding Full Path (%s --> %s) for %s', src, dst, nglib.user
    )
net1, net2 = src, dst
n1tree, n2tree = None, None
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', net1):
n1tree = nglib.query.net.get_net(net1, rtype='NGTREE')
if re.search('^\\d+\\.\\d+\\.\\d+\\.\\d+$', net2):
if n1tree:
n2tree = nglib.query.net.get_net(net2, rtype='NGTREE')
srctree, dsttree, srcswp, dstswp = None, None, None, None
net1 = n1tree['_child001']['Name']
if n2tree:
if nglib.use_netdb:
net2 = n2tree['_child001']['Name']
srctree = nglib.netdb.ip.get_netdb_ip(src)
if srctree:
dsttree = nglib.netdb.ip.get_netdb_ip(dst)
router = n1tree['_child001']['Router']
if dsttree:
if 'StandbyRouter' in n1tree['_child001']:
router = n2tree['_child001']['Router']
switching = True
router = router + '|' + n1tree['_child001']['StandbyRouter']
srcswp = get_switched_path(srctree['Switch'], router, verbose=False)
if 'StandbyRouter' in n2tree['_child001']:
if srctree and dsttree:
router = router + '|' + n2tree['_child001']['StandbyRouter']
dstswp = get_switched_path(router, dsttree['Switch'], verbose=False)
if srctree['Switch'] == dsttree['Switch'] and srctree['VLAN'] == dsttree['VLAN'
ngtree = nglib.ngtree.get_ngtree('L2-L4', tree_type='PATHs')
switching = False
if n1tree['_child001']['Name'] != n2tree['_child001']['Name']:
ngtree['L3 Path'] = net1 + ' -> ' + net2
if srctree and dsttree:
ngtree['Lx Path'] = src + ' -> ' + dst
ngtree['L2 Path'] = srctree['Switch'] + ' (' + srctree['SwitchPort'
    ] + ') -> ' + dsttree['Switch'] + ' (' + dsttree['SwitchPort'] + ')'
n1tree['_type'] = 'SRC'
n1tree['Name'] = src
nglib.ngtree.add_child_ngtree(ngtree, n1tree)
if not switching and '_child002' in n2tree:
nglib.ngtree.add_child_ngtree(n1tree, n2tree['_child002'])
if switching and srcswp:
n1tree['_type'] = 'L2PATH'
nglib.ngtree.add_child_ngtree(ngtree, srcswp)
rtree = get_full_routed_path(src, dst, rtype='NGTREE', l2path=True)
n1tree['Name'] = src + ' -> ' + dst
if rtree and 'PATH' in rtree['_type']:
if rtree['_type'] == 'L4-PATH':
if switching and dstswp:
ngtree['L4 Path'] = rtree['Name']
ngtree['L4 Path'] = 'VRF:' + n1tree['_child001']['VRF']
nglib.ngtree.add_child_ngtree(ngtree, dstswp)
if switching:
nglib.ngtree.add_child_ngtree(ngtree, rtree)
n2tree['_type'] = 'DST'
ngtree = nglib.query.exp_ngtree(ngtree, rtype)
n2tree['Name'] = dst
return ngtree
nglib.ngtree.add_child_ngtree(ngtree, n2tree)
